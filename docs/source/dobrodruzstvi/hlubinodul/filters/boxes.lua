-- boxes.lua — Pandoc Lua filter: ::: divs -> D&D 5e LaTeX boxes.
--
-- Supported divs (pandoc fenced_divs, enabled by default in markdown):
--   ::: squarebox    first line fully bold -> box title; tcolorbox, 5e styling
--   ::: readaloud    -> DndReadAloud env (upstream package)
--   ::: dnditem      line 1 = name, line 2 = type/rarity, rest = description
--   ::: dndmonster   leading `key: value` lines -> DndMonster stat block
--
-- Lines within a div are one pandoc block with LineBreak inlines, so all
-- handlers work at the line/inline level, not the block level.
--
-- Trick: the div is turned into an unclassed Div wrapping its own (already
-- filtered) content between raw \begin{...}/\end{...} blocks, so pandoc
-- renders the body normally and all markdown features keep working.

-- Escape a plain string for use inside a LaTeX argument.
local function esc(s)
  s = s:gsub('\\', '\\\\')
  s = s:gsub('{', '\\{')
  s = s:gsub('}', '\\}')
  s = s:gsub('#', '\\#')
  s = s:gsub('%$', '\\$')
  s = s:gsub('%&', '\\&')
  s = s:gsub('%%', '\\%')
  s = s:gsub('~~', '\\textasciitilde{}')
  s = s:gsub('_', '\\textunderscore')
  s = s:gsub('%^', '\\textasciicircum')
  s = s:gsub('|', '\\textbar{}')
  return s
end

-- Concatenate plain text of inlines in range [a, b] (emph/strong flattened,
-- LineBreak -> \n).
local function textof(inls, a, b)
  local buf = {}
  local function add(x)
    if x.t == 'Str' then
      buf[#buf + 1] = x.text
    elseif x.t == 'Space' then
      buf[#buf + 1] = ' '
    elseif x.t == 'LineBreak' or x.t == 'SoftBreak' then
      buf[#buf + 1] = '\n'
    elseif x.t == 'Emph' or x.t == 'Strong' or x.t == 'Strikeout' then
      for _, y in ipairs(x.c) do add(y) end
    elseif x.t == 'Code' then
      buf[#buf + 1] = x.text
    end
  end
  for i = a, b do
    if i <= #inls and i >= 1 then add(inls[i]) end
  end
  return table.concat(buf)
end

-- Plain text of a Para/Plain block.
local function blocktext(el)
  if el.t == 'Para' or el.t == 'Plain' then
    return textof(el.c, 1, #el.c)
  end
  return ''
end

-- Return div with content wrapped in raw begin/end, classes cleared.
local function wrap(div, begin_raw, end_raw, content)
  div.classes = {}
  div.attributes = {}
  local out = pandoc.List{ pandoc.RawBlock('latex', begin_raw) }
  out:extend(content or {})
  out:insert(pandoc.RawBlock('latex', end_raw))
  div.content = out
  return div
end

local function div(div)
  local cls = div.classes[1]
  if not cls or #div.content == 0 then return nil end

  -- ::: readaloud -> DndReadAloud
  if cls == 'readaloud' then
    return wrap(div, '\\begin{DndReadAloud}', '\\end{DndReadAloud}', div.content)
  end

  -- ::: squarebox -> squarebox (first fully-bold line becomes the title)
  if cls == 'squarebox' then
    -- line-based content (title + poem lines): make newlines real breaks
    if div.content[1] and div.content[1].c then
      local fc = div.content[1].c
      for i = 1, #fc do
        if fc[i].t == 'SoftBreak' then fc[i] = pandoc.LineBreak() end
      end
    end
    local content = div.content
    local begin_raw = '\\begin{squarebox}'
    local first = content[1]
    if first and first.t == 'Para'
        and first.c[1] and first.c[1].t == 'Strong'
        and #first.c >= 2
        and (first.c[2].t == 'LineBreak' or first.c[2].t == 'SoftBreak') then
      begin_raw = '\\begin{squarebox}[title={' .. esc(textof(first.c, 1, 1)) .. '}]'
      content = {}
      local rest = {}
      for idx = 3, #first.c do rest[#rest + 1] = first.c[idx] end
      if #rest > 0 then content[#content + 1] = pandoc.Para(rest) end
      for idx = 2, #div.content do content[#content + 1] = div.content[idx] end
    end
    return wrap(div, begin_raw, '\\end{squarebox}', content)
  end

  -- ::: dnditem -> dnditem (line 1 = name, line 2 = type/rarity)
  if cls == 'dnditem' then
    local first = div.content[1]
    local name, typ = nil, nil
    local body = {}
    if first and (first.t == 'Para' or first.t == 'Plain') then
      local inls = first.c
      -- name and type lines are line-based: make their newlines real
      -- breaks (first two only); the description stays soft-wrapped prose
      local nb = 0
      for i = 1, #inls do
        if inls[i].t == 'SoftBreak' or inls[i].t == 'LineBreak' then
          nb = nb + 1
          if inls[i].t == 'SoftBreak' then inls[i] = pandoc.LineBreak() end
          if nb >= 2 then break end
        end
      end
      local lbs = {}
      for idx, x in ipairs(inls) do
        if x.t == 'LineBreak' or x.t == 'SoftBreak' then lbs[#lbs + 1] = idx end
      end
      if #lbs >= 2 then
        name = textof(inls, 1, lbs[1] - 1)
        typ = textof(inls, lbs[1] + 1, lbs[2] - 1)
        local rest = {}
        for idx = lbs[2] + 1, #inls do rest[#rest + 1] = inls[idx] end
        if #rest > 0 and rest[1].t == 'Space' then table.remove(rest, 1) end
        if #rest > 0 then body[#body + 1] = pandoc.Para(rest) end
      elseif #lbs == 1 then
        name = textof(inls, 1, lbs[1] - 1)
        typ = textof(inls, lbs[1] + 1, #inls)
      else
        name = textof(inls, 1, #inls)
        typ = ''
      end
    else
      name = blocktext(first)
      typ = (#div.content >= 2) and blocktext(div.content[2]) or ''
    end
    if not name or name == '' or typ == '' then
      pandoc.log.warn('dnditem: needs line 1 = name, line 2 = type/rarity')
      return nil
    end
    for i = 2, #div.content do body[#body + 1] = div.content[i] end
    return wrap(div,
      '\\begin{dnditem}{' .. esc(name) .. '}{' .. esc(typ) .. '}',
      '\\end{dnditem}', body)
  end

  -- ::: dndmonster -> DndMonster stat block from key: value lines
  if cls == 'dndmonster' then
    local first = div.content[1]
    if not (first and (first.t == 'Para' or first.t == 'Plain')) then
      pandoc.log.warn('dndmonster: first block must be plain key: value lines')
      return nil
    end
    local text = blocktext(first)
    local lines = {}
    for line in (text .. '\n'):gmatch('([^\n]*)\n') do
      lines[#lines + 1] = line
    end

    local keys = {}
    local i = 1
    while i <= #lines do
      local k, v = lines[i]:match('^([%a_]+)%s*:%s*(.*)$')
      if not k then break end
      keys[k] = v
      i = i + 1
    end
    -- optional '---' line at the end of the key block
    if lines[i] and lines[i]:match('^%s*---%s*$') then i = i + 1 end

    if not keys.name then
      pandoc.log.warn('dndmonster: missing required key "name"')
      return nil
    end

    -- non-key lines left in the key block: start the body on its own
    -- paragraph (blank line before it) to keep markdown working
    local leftover = {}
    for j = i, #lines do
      if lines[j]:match('%S') then leftover[#leftover + 1] = lines[j] end
    end
    if #leftover > 0 then
      pandoc.log.warn('dndmonster: non-key lines in the key block — put the body after a blank line')
    end

    local body = {}
    local start = 2
    -- a horizontal rule right after the keys is the optional '---' separator
    if div.content[start] and div.content[start].t == 'HorizontalRule' then
      start = start + 1
    end
    for j = start, #div.content do body[#body + 1] = div.content[j] end

    -- a paragraph that is fully bold (e.g. "**Actions**") is a statblock
    -- section header -> \DndMonsterSection (red small caps + rule), not a
    -- bold body paragraph
    for j, blk in ipairs(body) do
      if blk.t == 'Para' and #blk.c == 1 and blk.c[1].t == 'Strong' then
        body[j] = pandoc.RawBlock('latex',
          '\\DndMonsterSection{' .. esc(textof(blk.c, 1, 1)) .. '}')
      end
    end

    local known = {
      name = 1, type = 1, armor_class = 1, hit_points = 1, speed = 1,
      str = 1, dex = 1, con = 1, int = 1, wis = 1, cha = 1,
      saving_throws = 1, skills = 1,
      damage_immunities = 1, damage_vulnerabilities = 1, damage_resistances = 1,
      condition_immunities = 1, senses = 1, languages = 1, challenge = 1,
    }
    for k in pairs(keys) do
      if not known[k] then
        pandoc.log.warn('dndmonster: unknown key "' .. k .. '" (ignored)')
      end
    end

    local b = {}
    if keys.armor_class then b[#b + 1] = 'armor-class={' .. esc(keys.armor_class) .. '}' end
    if keys.hit_points  then b[#b + 1] = 'hit-points={' .. esc(keys.hit_points) .. '}' end
    if keys.speed       then b[#b + 1] = 'speed={' .. esc(keys.speed) .. '}' end

    local abilities = {}
    for _, a in ipairs({ 'str', 'dex', 'con', 'int', 'wis', 'cha' }) do
      if keys[a] then abilities[#abilities + 1] = a .. '={' .. esc(keys[a]) .. '}' end
    end

    local details = {}
    for _, pair in ipairs({
      { 'saving_throws', 'saving-throws' },
      { 'skills', 'skills' },
      { 'damage_immunities', 'damage-immunities' },
      { 'damage_vulnerabilities', 'damage-vulnerabilities' },
      { 'damage_resistances', 'damage-resistances' },
      { 'condition_immunities', 'condition-immunities' },
      { 'senses', 'senses' },
      { 'languages', 'languages' },
      { 'challenge', 'challenge' },
    }) do
      if keys[pair[1]] then details[#details + 1] = pair[2] .. '={' .. esc(keys[pair[1]]) .. '}' end
    end

    -- padding: upstream DndMonsterBg uses left/right=2pt (too tight, text
    -- hugs the box border); override via tcolorbox options here
    local begin_raw = '\\begin{DndMonster}[float=htbp,left=6pt,right=6pt]{'
        .. esc(keys.name) .. '}'
    local mid = pandoc.List{}
    if keys.type then mid[#mid + 1] = pandoc.RawBlock('latex', '\\DndMonsterType{' .. esc(keys.type) .. '}') end
    if #b > 0 then mid[#mid + 1] = pandoc.RawBlock('latex', '\\DndMonsterBasics[' .. table.concat(b, ',') .. ']') end
    if #abilities > 0 then mid[#mid + 1] = pandoc.RawBlock('latex', '\\DndMonsterAbilityScores[' .. table.concat(abilities, ',') .. ']') end
    if #details > 0 then mid[#mid + 1] = pandoc.RawBlock('latex', '\\DndMonsterDetails[' .. table.concat(details, ',') .. ']') end

    mid:extend(body)
    return wrap(div, begin_raw, '\\end{DndMonster}', mid)
  end

  return nil
end

return { Div = div }
