class Pokemon:
    def __init__(self, name, type_, evolutions=None):
        self.name = name
        self.type = type_
        self.evolutions = evolutions or []

class Pokedex:
    def __init__(self):
        # Predefined list of Pokemons from the first generation
        self.pokemons = [
            Pokemon("Bulbasaur", "Grass/Poison", ["Ivysaur", "Venusaur"]),
            Pokemon("Charmander", "Fire", ["Charmeleon", "Charizard"]),
            Pokemon("Squirtle", "Water", ["Wartortle", "Blastoise"]),
            Pokemon("Caterpie", "Bug", ["Metapod", "Butterfree"]),
            Pokemon("Weedle", "Bug/Poison", ["Kakuna", "Beedrill"]),
            Pokemon("Pidgey", "Normal/Flying", ["Pidgeotto", "Pidgeot"]),
            Pokemon("Rattata", "Normal", ["Raticate"]),
            Pokemon("Spearow", "Normal/Flying", ["Fearow"]),
            Pokemon("Ekans", "Poison", ["Arbok"]),
            Pokemon("Pikachu", "Electric", ["Raichu"]),
            Pokemon("Sandshrew", "Ground", ["Sandslash"]),
            Pokemon("Nidoran♀", "Poison", ["Nidorina", "Nidoqueen"]),
            Pokemon("Nidoran♂", "Poison", ["Nidorino", "Nidoking"]),
            Pokemon("Clefairy", "Fairy", ["Clefable"]),
            Pokemon("Vulpix", "Fire", ["Ninetales"]),
            Pokemon("Jigglypuff", "Normal/Fairy", ["Wigglytuff"]),
            Pokemon("Zubat", "Poison/Flying", ["Golbat"]),
            Pokemon("Oddish", "Grass/Poison", ["Gloom", "Vileplume"]),
            Pokemon("Paras", "Bug/Grass", ["Parasect"]),
            Pokemon("Venonat", "Bug/Poison", ["Venomoth"]),
            Pokemon("Diglett", "Ground", ["Dugtrio"]),
            Pokemon("Pinsir", "Bug"),
            Pokemon("Tauros", "Normal"),
            Pokemon("Magikarp", "Water", ["Gyarados"]),
            Pokemon("Lapras", "Water/Ice"),
            Pokemon("Ditto", "Normal"),
            Pokemon("Aerodactyl", "Rock/Flying"),
            Pokemon("Snorlax", "Normal"),
            Pokemon("Articuno", "Ice/Flying"),
            Pokemon("Zapdos", "Electric/Flying"),
            Pokemon("Moltres", "Fire/Flying"),
            Pokemon("Dratini", "Dragon", ["Dragonair", "Dragonite"]),
            Pokemon("Mewtwo", "Psychic"),
            Pokemon("Mew", "Psychic"),
        ]

    def get_pokemon_info(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                return f"Name: {pokemon.name}, Type: {pokemon.type}"

        return f"Pokemon '{pokemon_name}' not found in the Pokedex."

    def has_evolutions(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                return bool(pokemon.evolutions)

        return f"Pokemon '{pokemon_name}' not found in the Pokedex."

# Example usage:
pokedex = Pokedex()

# Get information about a Pokemon
print(pokedex.get_pokemon_info("Bulbasaur"))

# Check if a Pokemon has evolutions
print(pokedex.has_evolutions("Bulbasaur"))
print(pokedex.has_evolutions("Charmander"))
print(pokedex.has_evolutions("Pikachu"))
