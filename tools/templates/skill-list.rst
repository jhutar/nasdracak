{% for entity in entities -%}
* {{ entity.name }}

  * Přidává bonus pro skupinu: {{ (entity.bonus | entity_by_id).name }}
  * Použití: {{ entity.description }}{% if entity.requires %}
  * Poznámka: {{ entity.note }}{% endif %}
  * Pravidlo: {{ entity.rule }}
  * Kdo může dovednost použít: {{ entity.who }}{% if entity.requires %}
  * Smíš se naučit pokud už umíš: {% for e in entity.requires %}{{ (e | entity_by_id).name }}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %}

{% endfor %}
