
import random

class Equipment:
    """Base class for items, weapons, and skills."""
    def __init__(self, name):
        self.name = name

class Armor(Equipment):
    """A piece of equipment that can be used to protect character from attack."""
    def __init__(self, name, defense):
        super().__init__(name)
        self.defense = defense

    def hook_defence_roll(self, combat_round):
        return self.defense

class Weapon(Equipment):
    """A piece of equipment that can be used for attack and defense."""
    def __init__(self, name, attack, defense):
        super().__init__(name)
        self.attack = attack
        self.defense = defense
        self._round = None

    def hook_attack_roll(self):
        return self.attack

    def hook_defence_roll(self, combat_round):
        """Weapon defence can be only used once per combat round."""
        if combat_round == self._round:
            return 0
        else:
            self._round = combat_round
            return self.defense

    def hook_reset(self):
        self._round = None

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
        self.equipment = []
        self.initial_health = health
        self.initial_mana = mana

    def roll_attack(self):
        """Calculates the attack score."""
        attack_bonus = 0
        for equip in self.equipment:
            if callable(getattr(equip, "hook_attack_roll", None)):
                attack_bonus += equip.hook_attack_roll()

        return random.randint(1, 6) + self.strength + attack_bonus

    def roll_defense(self, combat_round):
        """Calculates the defense score."""
        defence_bonus = 0
        for equip in self.equipment:
            if callable(getattr(equip, "hook_defence_roll", None)):
                defence_bonus += equip.hook_defence_roll(combat_round)

        return random.randint(1, 6) + self.dexterity + defence_bonus

    def is_alive(self):
        """Check if the character is still alive."""
        return self.health > 0

    def reset(self):
        """Resets character's health to its initial value."""
        self.health = self.initial_health
        self.mana = self.initial_mana
        for equip in self.equipment:
            if callable(getattr(equip, "hook_reset", None)):
                equip.hook_reset()


def _combat_groups(round_number, attacking_group, defending_group):
    for attacker in attacking_group:
        if not attacker.is_alive():
            continue

        alive_defenders = [d for d in defending_group if d.is_alive()]
        if not alive_defenders:
            break

        defender = random.choice(alive_defenders)

        attack_roll = attacker.roll_attack()
        defense_roll = defender.roll_defense(round_number)

        damage = attack_roll - defense_roll
        if damage > 0:
            defender.health -= damage
            print(f"V kole {round_number} '{attacker.name}' zranil '{defender.name}' za {damage} životů")


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
        print("Zvítězili hrdinové")
        return 1, round_number
    else:
        print("Zvítězili nepřátelé")
        return 2, round_number

# --- Simulation Setup ---
if __name__ == "__main__":
    # Create characters and equipment
    group1 = []
    warrior = Character(name="Válečník A", strength=3, dexterity=1, resistance=1, intelligence=0, charisma=-1, health=4, mana=3)
    warrior.equipment.append(Weapon(name="Rezavý krátký meč", attack=2, defense=2))
    warrior.equipment.append(Armor(name="Vycpávané brnění", defense=1))
    group1.append(warrior)
    ###mage = Character(name="Kouzelník B", strength=-1, dexterity=1, resistance=0, intelligence=+3, charisma=1, health=3, mana=6)
    ###mage.equipment.append(Weapon(name="Dýka", attack=1, defense=1))
    ###group1.append(mage)

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
        print(f"Začíná simulace {i}")
        winner, round_number = simulate_combat(group1, group2)
        if winner == 1:
            heros_wins += 1
        rounds_counter += round_number
            
    print(f"--- Výsledky simulace ---")
    print(f"Celkem simulací: {num_simulations}")
    print(f"Hrdinové vyhráli: {heros_wins} ({(heros_wins / num_simulations) * 100:.2f}%)")
    print(f"Nepřátelé vyhráli: {num_simulations - heros_wins} ({((num_simulations - heros_wins) / num_simulations) * 100:.2f}%)")
    print(f"Průměrný počet kol: {rounds_counter / num_simulations:.2f}")
