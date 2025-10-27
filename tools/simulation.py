
import random

def roll_1k6():
    return random.randint(1, 6)

class Equipment:
    """Base class for items, weapons, and skills."""
    def __init__(self, name):
        self.name = name

    def _hook_exists(self, name):
        return callable(getattr(self, name, None))

    def _hook_or_zero(self, name, *args):
        if self._hook_exists(name):
            return getattr(self, name)(*args)
        else:
            return 0

    def reset(self, character):
        pass


class Armor(Equipment):
    """A piece of equipment that can be used to protect character from attack."""
    def __init__(self, name, defense):
        super().__init__(name)
        self.defense = defense

    def roll_defense(self, character):
        return roll_1k6() + character.dexterity + self.defense

class Weapon(Equipment):
    """A piece of equipment that can be used for attack and defense."""
    def __init__(self, name, attack, defense):
        super().__init__(name)
        self.attack = attack
        self.defense = defense

    def roll_attack(self, character):
        return roll_1k6() + character.strength + self.attack

    def roll_defense(self, character):
        return roll_1k6() + character.dexterity + self.defense

class Spell(Equipment):
    """A spell that can be used for attack."""
    def __init__(self, name, mana, attack, defense_property=None, defense_armor=None):
        super().__init__(name)
        self.mana = mana
        self.attack = attack
        self.defense_property = defense_property
        self.defense_armor = defense_armor

    def is_usable(self, character):
        return character.mana >= self.mana

    def roll_attack(self, character):
        if self.mana > character.mana:
            raise Exception("Not enough mana: {self.mana} vs. {character.mana}")

        character.mana -= self.mana
        return roll_1k6() + character.intelligence + self.attack

class EquipmentList(list):
    def first_weapon(self):
        for i in self:
            if isinstance(i, Weapon):
                return i

    def all_armors(self):
        """Returns all pieces of armor but also weapon as some have non-0 defense bonus as well."""
        return [i for i in self if isinstance(i, Armor)] + [self.first_weapon()]

    def first_spell(self):
        for i in self:
            if isinstance(i, Spell):
                return i

class Attack:
    def __init__(self, attacker, defender, round_number):
        self.attacker = attacker
        self.defender = defender
        self.round_number = round_number

    def fight(self):
        weapon_choice = self.attacker.pick_attack()
        armor_choices = self.defender.pick_defense()

        attack_roll = weapon_choice.roll_attack(self.attacker)

        armor_bonus = sum([i.defense for i in armor_choices])

        if isinstance(weapon_choice, Spell):
            # Spells defines various way on how to protect from them
            defense_roll = roll_1k6()
            if weapon_choice.defense_property is not None:
                defense_roll += getattr(self.defender, weapon_choice.defense_property)
            if weapon_choice.defense_armor:
                defense_roll += armor_bonus
        else:
            # Defense from weapon is simply target's dexterity and armor
            defense_roll = roll_1k6() + self.defender.dexterity + armor_bonus

        damage = attack_roll - defense_roll
        if damage > 0:
            self.defender.health -= damage
            print(f"V kole {self.round_number} '{self.attacker.name}' pomocí '{weapon_choice.name}'({attack_roll}) zranil '{self.defender.name}'({defense_roll}) za {damage} životů")
        else:
            print(f"V kole {self.round_number} '{self.attacker.name}' použil '{weapon_choice.name}'({attack_roll}) proti '{self.defender.name}'({defense_roll}) ale minul")


class Character:
    """Base class for heroes and monsters."""
    def __init__(self, name, strength, dexterity, resistance, intelligence, charisma, health, mana):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.resistance = resistance
        self.intelligence = intelligence
        self.charisma = charisma
        self.health = health
        self.mana = mana
        self.equipment = EquipmentList()
        self.initial_health = health
        self.initial_mana = mana

    def pick_attack(self):
        """Pick how are we going to attack."""
        if e := self.equipment.first_spell():
            if e.is_usable(self):
                return e

        if e := self.equipment.first_weapon():
            return e

        return Weapon("Bare hands", -3, -3)

    def pick_defense(self):
        """Pick how are we going to defend ourselves."""
        if e := self.equipment.all_armors():
            return e

        return [Armor("Bare skin", 0)]

    def is_alive(self):
        """Check if the character is still alive."""
        return self.health > 0

    def reset(self):
        """Resets character's health to its initial value."""
        self.health = self.initial_health
        self.mana = self.initial_mana
        for e in self.equipment:
            e.reset(self)


def _combat_groups(round_number, attacking_group, defending_group):
    for attacker in attacking_group:
        if not attacker.is_alive():
            continue

        alive_defenders = [d for d in defending_group if d.is_alive()]
        if not alive_defenders:
            break

        defender = random.choice(alive_defenders)

        Attack(attacker, defender, round_number).fight()


def simulate_combat(group1, group2):
    """
    Simulates a single combat between two groups.
    Returns the winning group number (1 or 2).
    """
    # Reset health for all characters
    for char in group1 + group2:
        char.reset()

    # Initiative roll
    while True:
        initiative1 = random.randint(1, 6)
        initiative2 = random.randint(1, 6)
        if initiative1 != initiative2:
            break
    
    if initiative1 > initiative2:
        attacking_group, defending_group = group1, group2
    else:
        attacking_group, defending_group = group2, group1

    round_number = 0
    while any(char.is_alive() for char in group1) and any(char.is_alive() for char in group2):
        round_number += 1

        # First group attacks
        _combat_groups(round_number, attacking_group, defending_group)

        # Second group attacks
        _combat_groups(round_number, defending_group, attacking_group)

    if any(char.is_alive() for char in group1):
        print(f"V kole {round_number} zvítězili hrdinové")
        return 1, round_number
    else:
        print(f"V kole {round_number} zvítězili nepřátelé")
        return 2, round_number

# --- Simulation Setup ---
if __name__ == "__main__":
    # Create characters and equipment
    group1 = []
    ###warrior = Character(name="Válečník A", strength=3, dexterity=1, resistance=1, intelligence=0, charisma=-1, health=4, mana=3)
    ###warrior.equipment.append(Weapon(name="Rezavý krátký meč", attack=2, defense=2))
    ###warrior.equipment.append(Armor(name="Vycpávané brnění", defense=1))
    ###group1.append(warrior)
    mage = Character(name="Kouzelník B", strength=-1, dexterity=1, resistance=0, intelligence=+3, charisma=1, health=3, mana=6)
    mage.equipment.append(Weapon(name="Dýka", attack=1, defense=1))
    mage.equipment.append(Spell(name="Ledové kopí", mana=3, attack=2, defense_property="dexterity", defense_armor=True))
    group1.append(mage)

    group2 = []
    ###for i in range(1, 1 + 1):
    ###    rat = Character(name=f"Krysa {i}", strength=-1, dexterity=1, resistance=1, intelligence=-3, charisma=-3, health=1, mana=0)
    ###    rat.equipment.append(Weapon(name="Zuby", attack=1, defense=0))
    ###    group2.append(rat)
    for i in range(1, 1 + 1):
        wolf = Character(name=f"Vlk {i}", strength=1, dexterity=2, resistance=1, intelligence=-3, charisma=-3, health=4, mana=0)
        wolf.equipment.append(Weapon(name="Tesáky", attack=2, defense=1))
        group2.append(wolf)

    # Run simulations
    num_simulations = 1000
    heros_wins = 0
    rounds_counter = 0
    
    for i in range(num_simulations):
        print(f"Začíná simulace #{i}")
        winner, round_number = simulate_combat(group1, group2)
        if winner == 1:
            heros_wins += 1
        rounds_counter += round_number
            
    print(f"--- Výsledky simulace ---")
    print(f"Celkem simulací: {num_simulations}")
    print(f"Hrdinové vyhráli: {heros_wins} ({(heros_wins / num_simulations) * 100:.2f}%)")
    print(f"Nepřátelé vyhráli: {num_simulations - heros_wins} ({((num_simulations - heros_wins) / num_simulations) * 100:.2f}%)")
    print(f"Průměrný počet kol: {rounds_counter / num_simulations:.2f}")
