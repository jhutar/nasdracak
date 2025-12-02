{% for entity in entities -%}
* {{ entity.name }}

  * Přidává bonus pro skupinu: {{ entity.bonus }}
  * Použití: {{ entity.description }}
  * Pravidlo: TODO
  * Kdo může dovednost použít: TODO{% if entity.requires %}
  * Smíš se naučit pokud už umíš: {{ entity.requires | join(', ') }}{% endif %}

{% endfor %}
