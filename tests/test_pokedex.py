import unittest

from app.pokedex import Pokedex

class TestPokedex(unittest.TestCase):

    def setUp(self):
        self.pokedex = Pokedex()

    def test_get_pokemon_info(self):
        self.assertEqual(self.pokedex.get_pokemon_info("Bulbasaur"), "Name: Bulbasaur, Type: Grass/Poison")
        self.assertEqual(self.pokedex.get_pokemon_info("Pikachu"), "Name: Pikachu, Type: Electric")
        self.assertEqual(self.pokedex.get_pokemon_info("Mewtwo"), "Name: Mewtwo, Type: Psychic")
        self.assertEqual(self.pokedex.get_pokemon_info("NonExistentPokemon"), "Pokemon 'NonExistentPokemon' not found in the Pokedex.")

    def test_has_evolutions(self):
        self.assertTrue(self.pokedex.has_evolutions("Bulbasaur"))
        self.assertTrue(self.pokedex.has_evolutions("Pikachu"))
        self.assertFalse(self.pokedex.has_evolutions("Ditto"))  # Ditto has no evolutions
        self.assertEqual(self.pokedex.has_evolutions("NonExistentPokemon"), "Pokemon 'NonExistentPokemon' not found in the Pokedex.")
