.. csv-table:: Dovednosti
   :header: "Dovednost", "Skupina", "Pravidlo", "Kdo může použít", "Vyžaduje"
   :class: longtable

   {% for entity in entities -%}
   "{{ entity.name }}", "{{ entity.bonus }}", "{{ entity.rule }}", "{{ entity.who }}", "{{ entity.requires | join(', ') }}"
   {% endfor %}
