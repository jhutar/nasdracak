.. csv-table:: Dovednosti
   :header: "Dovednost", "Skupina", "Pravidlo", "Vyžaduje"

   {% for entity in entities -%}
   "{{ entity.name }}", "{{ entity.bonus }}", "TODO", "{{ entity.requires | join(', ') }}"
   {% endfor %}
