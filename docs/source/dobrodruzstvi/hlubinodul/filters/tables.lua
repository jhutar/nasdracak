-- tables.lua — Pandoc Lua filter: rewrite Table AST as raw DndTable env.
--
-- The LaTeX writer always emits longtable, which fails in twocolumn mode
-- ("longtable not in 1-column mode"). We render cells to LaTeX ourselves
-- and emit the dnd package's DndTable (tabularx-based) instead.

-- Render a list of blocks to an inline LaTeX fragment.
local function blocks_to_latex(blocks)
  local out = {}
  for _, b in ipairs(blocks) do
    if b.t == 'Plain' or b.t == 'Para' then
      local p = pandoc.write(pandoc.Pandoc({ pandoc.Plain(b.c) }), 'latex')
      out[#out + 1] = p:gsub('[\r\n]+', ' ')
    else
      local p = pandoc.write(pandoc.Pandoc({ b }), 'latex')
      out[#out + 1] = p:gsub('[\r\n]+', ' ')
    end
  end
  return table.concat(out, ' '):gsub('%s+$', '')
end

-- Map a pandoc alignment to a tabularx column spec (X = stretch to line width).
local function colspec(align)
  if align == 'AlignCenter' then
    return '>{\\centering\\arraybackslash}X'
  elseif align == 'AlignRight' then
    return '>{\\raggedleft\\arraybackslash}X'
  end
  return 'X'
end

-- Collect plain text of a list of rows (each row = list of cells).
local function render_row(row)
  local cells = {}
  for _, cell in ipairs(row.cells) do
    cells[#cells + 1] = blocks_to_latex(cell.contents)
  end
  return table.concat(cells, ' & ') .. ' \\\\'
end

local function render_table(tbl)
  local cols = {}
  for _, spec in ipairs(tbl.colspecs or {}) do
    cols[#cols + 1] = colspec(spec[1])
  end
  if #cols == 0 then return nil end

  local lines = { '\\begin{DndTable}{' .. table.concat(cols) .. '}' }
  -- header row (if any)
  if tbl.head and #tbl.head.rows > 0 then
    for _, row in ipairs(tbl.head.rows) do
      lines[#lines + 1] = render_row(row)
    end
  end
  -- body rows (TableBody field layout varies across pandoc versions:
  -- body.body may be the row list itself, a {rows=...} table, or absent)
  for _, body in ipairs(tbl.bodies or {}) do
    local rows = body.body or body.rows or {}
    if rows.rows then rows = rows.rows end
    for _, row in ipairs(rows) do
      lines[#lines + 1] = render_row(row)
    end
  end
  lines[#lines + 1] = '\\end{DndTable}'
  return pandoc.RawBlock('latex', table.concat(lines, '\n'))
end

return { Table = render_table }
