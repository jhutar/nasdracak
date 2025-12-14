.. csv-table:: Zbraně pro boj na blízko
   :header: "Předmět", "Síla", "Cena"
   :class: longtable

   {% for entity in entities -%}
   "{{ entity.name }}: {{ entity.description }}", "{{ entity.demage }}", "{{ entity.price }} zlatých"
   {% endfor %}
