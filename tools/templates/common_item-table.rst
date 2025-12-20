.. csv-table:: Běžné předměty
   :header: "Předmět", "Cena"
   :class: longtable

   {% for entity in entities | sort(attribute='price') -%}
   "*{{ entity.name }}:* {{ entity.description }}", "{{ entity.price | format_price }}"
   {% endfor %}
