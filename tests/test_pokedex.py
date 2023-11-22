import unittest

from app.pokedex import Pokedex

class TestPokedex(unittest.TestCase):

    def setUp(self):
        self.pokedex = Pokedex()

    def test_get_pokemon_info_WHEN_pokemon_exists_RETURNS_pokemon_info(self):
        pokemon = "Bulbasaur";
        expected = "Name: Bulbasaur, Type: Grass/Poison"
        actual = self.pokedex.get_pokemon_info(pokemon)
        self.assertEqual(actual, expected)
    
    def test_get_pokemon_info_WHEN_pokemon_does_not_exist_RETURNS_error_message(self):
        pokemon = "NonExistentPokemon";
        expected = "Pokemon 'NonExistentPokemon' not found in the Pokedex."
        actual = self.pokedex.get_pokemon_info(pokemon)
        self.assertEqual(actual, expected)

    def test_get_pokemon_info_WHEN_pokemon_name_is_empty_RETURNS_error_message(self):
        pokemon = "";
        expected = "Pokemon '' not found in the Pokedex."
        actual = self.pokedex.get_pokemon_info(pokemon)
        self.assertEqual(actual, expected)
    
    def test_has_evolutions_WHEN_pokemon_has_evolutions_RETURNS_true(self):
        pokemon = "Bulbasaur";
        expected = True
        actual = self.pokedex.has_evolutions(pokemon)
        self.assertEqual(actual, expected)
    
    def test_has_evolutions_WHEN_pokemon_has_no_evolutions_RETURNS_false(self):
        pokemon = "Ditto";
        expected = False
        actual = self.pokedex.has_evolutions(pokemon)
        self.assertEqual(actual, expected)