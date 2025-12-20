.. csv-table:: Zbraně pro boj na blízko
   :header: "Předmět", "Síla", "Cena"
   :class: longtable

   {% for entity in entities | sort(attribute='price') -%}
   "*{{ entity.name }}:* {{ entity.description }}", "{{ entity.demage }}", "{{ entity.price | format_price }}"
   {% endfor %}
