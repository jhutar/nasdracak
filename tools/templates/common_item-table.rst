.. csv-table:: Běžné předměty
   :header: "Předmět", "Cena"
   :class: longtable

   {% for entity in entities -%}
   "{{ entity.name }}: {{ entity.description }}", "{{ entity.price }} zlatých"
   {% endfor %}
