import unittest
from animal import Animal
from animal import Dog


class TestAnimal(unittest.TestCase):

    # This is setting an instance that we can use repeatedly
    @classmethod
    def setUpClass(cls):
        cls.bob = Dog("Bob")

# Since this test is about the creation of a dog in general, we want to create a new instance
    def test_animal_creation(self):
        murph = Dog("Murph")
        self.assertIsInstance(murph, Dog)
        self.assertIsInstance(murph, Animal)

    def test_dog_has_name(self):
        result = self.bob.get_name()
        expected = "Bob"
        self.assertEqual(result, expected)

    def test_can_set_species(self):
        self.assertEqual(self.bob.get_species(), "Dog")
        self.bob.set_species("Canine")
        self.assertEqual(self.bob.get_species(), "Canine")

    def test_animal_walking_legless(self):
        animal = Animal()
        with self.assertRaises(ValueError):
            animal.walk()

    def test_animal_walking(self):
        animal = Animal()
        animal.set_legs(12)
        animal.walk()
        expected = 1.2
        result = animal.speed
        self.assertEqual(result, expected)

    def test_dog_walking_legless(self):
        dog = Dog("Doggo")
        with self.assertRaises(ValueError):
            dog.walk()

    def test_dog_walking(self):
        dog = Dog("Goodboy")
        dog.set_legs(4)
        dog.walk()
        expected = 0.8
        result = dog.speed
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
