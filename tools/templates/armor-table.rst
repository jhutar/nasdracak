.. csv-table:: Brnění
   :header: "Předmět", "Obrana", "Cena"
   :class: longtable

   {% for entity in entities | sort(attribute='price') -%}
   "*{{ entity.name }}:* {{ entity.description }}", "{{ entity.defense }}", "{{ entity.price | format_price }}"
   {% endfor %}
