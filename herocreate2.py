import tkinter as tk
from tkinter import ttk, messagebox

class HeroGUI:
    def __init__(self, root):
        self.root = root
        root.title("D&D Character Creator")

        # Hero details
        self.stats = {'Strength': tk.IntVar(value=10),
                      'Dexterity': tk.IntVar(value=10),
                      'Constitution': tk.IntVar(value=10),
                      'Intelligence': tk.IntVar(value=10),
                      'Wisdom': tk.IntVar(value=10),
                      'Charisma': tk.IntVar(value=10)}
        self.character_name = tk.StringVar(value=self.generate_name())
        self.gender_options = ["Prefer not to say", "Female", "Male", "Non-binary", "Transgender", "Genderfluid", "Agender", "Other"]
        self.gender = tk.StringVar()
        self.classes = [
            "Barbarian",
            "Bard",
            "Cleric",
            "Druid",
            "Fighter",
            "Monk",
            "Paladin",
            "Ranger",
            "Rogue",
            "Sorcerer",
            "Warlock",
            "Wizard"
        ]

        self.selected_class = tk.StringVar()        
        self.class_stats = {
            "Barbarian": {"Strength": 15, "Dexterity": 12, "Constitution": 14, "Intelligence": 8, "Wisdom": 10, "Charisma": 10},
            "Bard": {"Strength": 10, "Dexterity": 14, "Constitution": 12, "Intelligence": 12, "Wisdom": 10, "Charisma": 15},
            "Cleric": {"Strength": 10, "Dexterity": 10, "Constitution": 12, "Intelligence": 12, "Wisdom": 15, "Charisma": 12},
            "Druid": {"Strength": 10, "Dexterity": 12, "Constitution": 12, "Intelligence": 12, "Wisdom": 15, "Charisma": 10},
            "Fighter": {"Strength": 15, "Dexterity": 12, "Constitution": 14, "Intelligence": 10, "Wisdom": 10, "Charisma": 10},
            "Monk": {"Strength": 12, "Dexterity": 15, "Constitution": 14, "Intelligence": 10, "Wisdom": 12, "Charisma": 8},
            "Paladin": {"Strength": 14, "Dexterity": 10, "Constitution": 13, "Intelligence": 10, "Wisdom": 12, "Charisma": 14},
            "Ranger": {"Strength": 12, "Dexterity": 15, "Constitution": 12, "Intelligence": 12, "Wisdom": 14, "Charisma": 10},
            "Rogue": {"Strength": 8, "Dexterity": 15, "Constitution": 12, "Intelligence": 14, "Wisdom": 10, "Charisma": 12},
            "Sorcerer": {"Strength": 8, "Dexterity": 12, "Constitution": 12, "Intelligence": 12, "Wisdom": 10, "Charisma": 15},
            "Warlock": {"Strength": 10, "Dexterity": 12, "Constitution": 12, "Intelligence": 12, "Wisdom": 12, "Charisma": 15},
            "Wizard": {"Strength": 8, "Dexterity": 10, "Constitution": 12, "Intelligence": 15, "Wisdom": 14, "Charisma": 10}
        }
        self.race_stats_bonus = {
            "Human": {"Strength": 1, "Dexterity": 1, "Constitution": 1, "Intelligence": 1, "Wisdom": 1, "Charisma": 1},
            "Elf": {"Dexterity": 2, "Intelligence": 1},
            "Dwarf": {"Constitution": 2, "Strength": 1},
            "Halfling": {"Dexterity": 2, "Charisma": 1},
            "Dragonborn": {"Strength": 2, "Charisma": 1},
            "Gnome": {"Intelligence": 2, "Constitution": 1},
            "Half-Elf": {"Charisma": 2, "Dexterity": 1, "Wisdom": 1},
            "Half-Orc": {"Strength": 2, "Constitution": 1},
            "Tiefling": {"Intelligence": 1, "Charisma": 2},
            "Aarakocra": {"Dexterity": 2, "Wisdom": 1},
            "Genasi": {"Constitution": 2, "Strength": 1},
            "Goliath": {"Strength": 2, "Constitution": 1},
            "Aasimar": {"Charisma": 2, "Wisdom": 1},
            "Bugbear": {"Strength": 2, "Dexterity": 1},
            "Firbolg": {"Wisdom": 2, "Strength": 1},
            "Goblin": {"Dexterity": 2, "Constitution": 1},
            "Hobgoblin": {"Constitution": 2, "Intelligence": 1},
            "Kenku": {"Dexterity": 2, "Wisdom": 1},
            "Kobold": {"Dexterity": 2, "Strength": 1},
            "Lizardfolk": {"Constitution": 2, "Wisdom": 1},
            "Orc of Exandria": {"Strength": 2, "Constitution": 1},
            "Tabaxi": {"Dexterity": 2, "Charisma": 1},
            "Triton": {"Constitution": 2, "Strength": 1},
            "Yuan-ti Pureblood": {"Intelligence": 2, "Charisma": 1},
            "Feral Tiefling": {"Dexterity": 2, "Charisma": 1},
            "Tortle": {"Strength": 2, "Wisdom": 1},
            "Changeling": {"Charisma": 2, "Dexterity": 1},
            "Kalashtar": {"Charisma": 2, "Wisdom": 1},
            "Shifter": {"Dexterity": 2, "Wisdom": 1},
            "Warforged": {"Constitution": 2, "Strength": 1},
            "Centaur": {"Strength": 2, "Wisdom": 1},
            "Loxodon": {"Constitution": 2, "Wisdom": 1},
            "Minotaur": {"Strength": 2, "Constitution": 1},
            "Simic Hybrid": {"Constitution": 2, "Strength": 1},
            "Vedalken": {"Intelligence": 2, "Wisdom": 1},
            "Verdan": {"Constitution": 2, "Dexterity": 1},
            "Leonin": {"Strength": 2, "Charisma": 1},
            "Satyr": {"Charisma": 2, "Dexterity": 1},
            "Faerie": {"Dexterity": 2, "Charisma": 1},
            "Harengon": {"Dexterity": 2, "Intelligence": 1},
            "Owlin": {"Wisdom": 2, "Dexterity": 1},
            "Rabbitfolk": {"Dexterity": 2, "Wisdom": 1},
            "Reborn": {"Constitution": 2, "Charisma": 1},
            "Hexblood": {"Charisma": 2, "Constitution": 1},
            "Fairy": {"Dexterity": 2, "Charisma": 1},
            "Hobgoblin of the Feywild": {"Constitution": 2, "Intelligence": 1},
            "Owlfolk": {"Wisdom": 2, "Dexterity": 1},
            "Merfolk": {"Constitution": 2, "Dexterity": 1},
            "Vampire": {"Charisma": 2, "Strength": 1},
            "Dhampir": {"Charisma": 2, "Dexterity": 1},
            "Plasmoid": {"Constitution": 2, "Dexterity": 1},
            "Thri-kreen": {"Dexterity": 2, "Constitution": 1},
            "Giff": {"Constitution": 2, "Strength": 1},
            "Autognome": {"Intelligence": 2, "Dexterity": 1},
            "Gift Yankee": {"Charisma": 2, "Intelligence": 1},
            "Hadozee": {"Dexterity": 2, "Charisma": 1},
            "Shadow Elf": {"Dexterity": 2, "Intelligence": 1},
            "Spellweaver": {"Intelligence": 2, "Wisdom": 1},
            "Phoenixborn": {"Constitution": 2, "Charisma": 1},
            "Moirai": {"Charisma": 2, "Wisdom": 1},
            "Aetherborn": {"Charisma": 2, "Constitution": 1},
            "Voidwalker": {"Intelligence": 2, "Dexterity": 1},
            "Spirit Folk": {"Wisdom": 2, "Dexterity": 1},
            "Dragonkin": {"Strength": 2, "Constitution": 1},
            "Celestial-born": {"Charisma": 2, "Wisdom": 1},
            "Demi-God": {"Strength": 2, "Charisma": 1},
            "Elemental": {"Constitution": 2, "Intelligence": 1},
            "Mythborn": {"Strength": 2, "Charisma": 1},
            "Nephilim": {"Charisma": 2, "Strength": 1},
            "Shade": {"Dexterity": 2, "Charisma": 1},
            "Sylph": {"Dexterity": 2, "Wisdom": 1},
            "Undine": {"Constitution": 2, "Wisdom": 1},
            "Valkyrie": {"Strength": 2, "Charisma": 1},
            "Witchborn": {"Charisma": 2, "Intelligence": 1},
            "Eldritch Spawn": {"Charisma": 2, "Constitution": 1},
            "Arcanaborn": {"Intelligence": 2, "Wisdom": 1}
        }

        self.races = [
            "Human", "Elf", "Dwarf", "Halfling", "Orc",
            "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling",
            "Aarakocra", "Genasi", "Goliath", "Aasimar", "Bugbear",
            "Firbolg", "Goblin", "Hobgoblin", "Kenku", "Kobold",
            "Lizardfolk", "Orc of Exandria", "Tabaxi", "Triton", "Yuan-ti Pureblood",
            "Feral Tiefling", "Tortle", "Changeling", "Kalashtar", "Shifter",
            "Warforged", "Centaur", "Loxodon", "Minotaur", "Simic Hybrid",
            "Vedalken", "Verdan", "Leonin", "Satyr", "Aarakocra",
            "Faerie", "Harengon", "Owlin", "Rabbitfolk", "Reborn",
            "Hexblood", "Fairy", "Hobgoblin of the Feywild", "Owlfolk",
            "Goliath", "Merfolk", "Vampire", "Dhampir", "Plasmoid",
            "Thri-kreen", "Giff", "Autognome", "Gift Yankee", "Hadozee",
            "Shadow Elf", "Spellweaver", "Phoenixborn", "Moirai", "Aetherborn",
            "Voidwalker", "Spirit Folk", "Dragonkin", "Celestial-born", "Demi-God",
            "Elemental", "Mythborn", "Nephilim", "Shade", "Sylph",
            "Undine", "Valkyrie", "Witchborn", "Eldritch Spawn", "Arcanaborn"
        ]        

        self.selected_race = tk.StringVar()

        # Stats and abilities
        self.stats = {'Strength': tk.IntVar(),
                      'Dexterity': tk.IntVar(),
                      'Constitution': tk.IntVar(),
                      'Intelligence': tk.IntVar(),
                      'Wisdom': tk.IntVar(),
                      'Charisma': tk.IntVar()}
        self.abilities_list = ["Fireball", "Healing Touch", "Lightning Bolt", "Invisibility"]
        self.selected_ability = tk.StringVar()
        self.stats_labels = []  # Add this line here
        self.create_widgets()
        self.update_stats_display()  # Call this method to display default stats immediately


    def create_widgets(self):
        tk.Label(self.root, text="Name:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.character_name).grid(row=0, column=1)

        tk.Label(self.root, text="Gender:").grid(row=1, column=0)
        gender_dropdown = ttk.Combobox(self.root, textvariable=self.gender, values=self.gender_options, state="readonly")
        gender_dropdown.grid(row=1, column=1)
        gender_dropdown.current(0)

        tk.Label(self.root, text="Race:").grid(row=2, column=0)
        race_dropdown = ttk.Combobox(self.root, textvariable=self.selected_race, values=self.races, state="readonly")
        race_dropdown.grid(row=2, column=1)
        race_dropdown.current(0)
        self.selected_race.trace_add('write', self.update_stats_display)


        tk.Label(self.root, text="Class:").grid(row=3, column=0)
        class_dropdown = ttk.Combobox(self.root, textvariable=self.selected_class, values=self.classes, state="readonly")
        class_dropdown.grid(row=3, column=1)
        class_dropdown.current(0)
        self.selected_class.trace_add('write', self.update_stats_display) # Attach callback


        tk.Label(self.root, text="Choose Ability:").grid(row=4, column=0)
        abilities_dropdown = ttk.Combobox(self.root, textvariable=self.selected_ability, values=self.abilities_list, state="readonly")
        abilities_dropdown.grid(row=4, column=1)
        abilities_dropdown.current(0)

        tk.Button(self.root, text="Create Hero", command=self.create_hero).grid(row=5, columnspan=2)

    def create_hero(self):
        # Display hero stats in a new window
        display_window = tk.Toplevel(self.root)
        display_window.title("Hero Stats and Inventory")

        tk.Label(display_window, text=f"Name: {self.character_name.get()}").grid(row=0, column=0, columnspan=2)
        tk.Label(display_window, text=f"Gender: {self.gender.get()}").grid(row=1, column=0, columnspan=2)
        tk.Label(display_window, text=f"Race: {self.selected_race.get()}").grid(row=2, column=0, columnspan=2)
        tk.Label(display_window, text=f"Class: {self.selected_class.get()}").grid(row=3, column=0, columnspan=2)
        tk.Label(display_window, text=f"Selected Ability: {self.selected_ability.get()}").grid(row=4, column=0, columnspan=2)

        # Add a button to display ability description
        ability_button = tk.Button(display_window, text="Ability Description", command=self.show_ability_description)
        ability_button.grid(row=5, column=0, columnspan=2)
        
        

        # Inventory section
        tk.Label(display_window, text="Inventory:").grid(row=6, column=0)
        self.inventory_listbox = tk.Listbox(display_window)
        self.inventory_listbox.grid(row=7, column=0, columnspan=2)

        self.item_entry = tk.Entry(display_window)
        self.item_entry.grid(row=8, column=0)
        tk.Button(display_window, text="Add Item", command=self.add_item).grid(row=8, column=1)

        # Close the original window
        self.root.withdraw()
    def show_ability_description(self):
        ability_name = self.selected_ability.get()
        description = self.ability_descriptions.get(ability_name, "No description available")
        messagebox.showinfo("Ability Description", description)
    def add_item(self):
        item = self.item_entry.get()
        if item:
            self.inventory_listbox.insert(tk.END, item)
            self.item_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Item name cannot be empty.")

        self.ability_descriptions = {
            "Fireball": "This ability allows you to cast a fireball spell, dealing damage to all enemies within range.",
            "Healing Touch": "This ability allows you to heal wounds by touch, restoring health to yourself or allies.",
            "Lightning Bolt": "This ability allows you to summon a bolt of lightning, striking a single target for high damage.",
            "Invisibility": "This ability allows you to become invisible to enemies, making it easier to sneak past them."
        }

    # This method should be aligned with the other methods, not nested inside any of them.
    def show_ability_description(self):
        ability_name = self.selected_ability.get()
        description = self.ability_descriptions.get(ability_name, "No description available")
        messagebox.showinfo("Ability Description", description)    
    
    def update_stats_display(self, *args):
        # Clear existing stats labels
        for label in self.stats_labels:
            label.destroy()
        self.stats_labels.clear()

        # Base stats according to class
        selected_class = self.selected_class.get()
        class_stats = self.class_stats.get(selected_class, {})
        
        # Get racial bonuses
        selected_race = self.selected_race.get()
        race_bonus = self.race_stats_bonus.get(selected_race, {})

        # Combine class stats and racial bonuses
        combined_stats = {stat: class_stats.get(stat, 10) + race_bonus.get(stat, 0) for stat in self.stats}

        # Display the stats
        row_start = 9
        for stat, value in combined_stats.items():
            stat_label = tk.Label(self.root, text=f"{stat}: {value}")
            stat_label.grid(row=row_start, column=0, columnspan=2)
            self.stats_labels.append(stat_label)
            row_start += 1

    def generate_name(self):
        # Assuming you have a name generation method
        return "Character Name"

def main():
    root = tk.Tk()
    app = HeroGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
