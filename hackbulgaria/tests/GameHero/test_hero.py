from hero import Hero
import unittest
class TestHero(unittest.TestCase):
	def test_hero_init(self):
		hero = Hero("Born", 100, "DragonSlayer")
		self.assertEqual(hero.name,"Born")
		self.assertEqual(hero.health, 100)
		self.assertEqual(hero.nickname,"DragonSlayer")

	def test_known_as(self):
		hero = Hero("Bron", 100, "DragonSlayer")
		self.assertEqual(hero.known_as(),"Bron the DragonSlayer")

	def test_get_health(self):
		hero = Hero("Bron", 100, "DragonSlayer")
		self.assertEqual(100, hero.get_health())

	def test_is_alive(self):
		hero = Hero("Bron", 100, "DragonSlayer")
		self.assertTrue(hero.is_alive())

	def test_is_alive_death(self):
		hero = Hero("Bron", 100, "DragonSlayer")
		hero.health = 0
		self.assertFalse(hero.is_alive())

	def test_take_damage(self):
		hero = Hero("Bron", 100, "DragonSlayer")
		self.assertEqual(hero.take_damage(80),20)

	def test_take_damage_more(self):
		hero = Hero("Bron", 100, "DragonSlayer")
		self.assertEqual(hero.take_damage(123),0)
		
	def test_take_healing_deathed_hero(self):
		hero = Hero("Bron", 100, "DragonSlayer")
		hero.health = 0
		self.assertFalse(hero.take_healing(10))

	def test_take_healing(self):
		hero = Hero("Bron", 100, "DragonSlayer")
		self.assertTrue(hero.take_healing(10))

	def test_take_healing_limit_health_invalid(self):
		hero = Hero("Bron", 100, "DragonSlayer")
		hero.take_healing(10)
		self.assertEqual(100, hero.health)

	def test_take_healing_limit_health_valid(self):
		hero = Hero("Bron", 80, "DragonSlayer")
		hero.take_healing(10)
		self.assertEqual(90, hero.health)








if __name__ == '__main__':
	main()