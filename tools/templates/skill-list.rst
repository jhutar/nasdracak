{% for entity in entities -%}
* {{ entity.name }}

  * Přidává bonus pro skupinu: {{ entity.bonus }}
  * Použití: {{ entity.description }}{% if entity.requires %}
  * Poznámka: {{ entity.note }}{% endif %}
  * Pravidlo: {{ entity.rule }}
  * Kdo může dovednost použít: {{ entity.who }}{% if entity.requires %}
  * Smíš se naučit pokud už umíš: {{ entity.requires | join(', ') }}{% endif %}

{% endfor %}
