.. csv-table:: Běžné předměty
   :header: "Předmět", "Cena"

   {% for entity in entities -%}
   "{{ entity.name }}: {{ entity.description }}", "{{ entity.price }} zlatých"
   {% endfor %}
