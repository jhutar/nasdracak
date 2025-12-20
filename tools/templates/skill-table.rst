.. csv-table:: Dovednosti
   :header: "Dovednost", "Skupina", "Pravidlo", "Kdo může použít", "Vyžaduje"
   :class: longtable

   {% for entity in entities -%}
   "{{ entity.name }}", "{{ (entity.bonus | entity_by_id).name }}", "{{ entity.rule }}", "{{ entity.who }}", "{% for e in entity.requires %}{{ (e | entity_by_id).name }}{% if not loop.last %}, {% endif %}{% endfor %}"
   {% endfor %}
