{% for entity in entities -%}
* {{ entity.name }}

  * Použití kouzla: {{ entity.description }}
  * Pravidlo: {{ entity.rule }}

{% endfor %}
