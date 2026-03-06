**{{ entity.name }} ({{ (entity.race | entity_by_id).name }}, level {{ entity.level }})**

.. list-table:: Vlastnosti {{ entity.name }}
   :header-rows: 1

   * - SÍL
     - OBR
     - INT
     - CHAR
     - zdraví
     - magie
   * - {{ entity.strength }}
     - {{ entity.dexterity }}
     - {{ entity.inteligence }}
     - {{ entity.charisma }}
     - {{ entity.health_max }}
     - {{ entity.magenergy_max }}

* Výskyt: {{ (entity.location | entity_by_id).name }}
* Vzhled: {{ entity.appearance }}
* Inventář: {{ entity.inventory | join(', ') }}
* Pozadí: {{ entity.background }}
