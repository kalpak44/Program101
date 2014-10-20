from orc import Orc
import unittest

class TestOrc(unittest.TestCase):
	def setUp(self):
		self.orc = Orc("Monster", 100, 2)

	def test_orc_init(self):
		self.assertEqual(self.orc.name, "Monster")
		self.assertEqual(self.orc.health, 100)
		self.assertEqual(self.orc.berserk_factor, 2)

	def test_orc_limit_bf_more(self):
		orc = Orc("Monster", 100, 5)
		with self.assertRaises(ValueError):
			Orc(2)

	def test_orc_limit_bf_more(self):
		orc = Orc("Monster", 100, 1)
		self.assertEqual(orc.berserk_factor, 1)

	def test_orc_limit_bf_more(self):
		orc = Orc("Monster", 100, 2)
		self.assertEqual(orc.berserk_factor, 2)
	
	def test_get_health(self):
		self.assertEqual(100, self.orc.get_health())

	def test_is_alive(self):
		self.assertTrue(self.orc.is_alive())

	def test_is_alive_death(self):
		self.orc.health = 0
		self.assertFalse(self.orc.is_alive())

	def test_take_damage(self):
		self.assertEqual(self.orc.take_damage(80),20)

	def test_take_damage_more(self):
		self.assertEqual(self.orc.take_damage(123),0)
		
	def test_take_healing_deathed_hero(self):
		self.orc.health = 0
		self.assertFalse(self.orc.take_healing(10))

	def test_take_healing(self):
		self.assertTrue(self.orc.take_healing(10))

	def test_take_healing_limit_health_invalid(self):
		self.orc.take_healing(10)
		self.assertEqual(100, self.orc.health)

	def test_take_healing_limit_health_valid(self):
		self.orc.health = 80
		self.orc.take_healing(10)
		self.assertEqual(90, self.orc.health)










if __name__ == '__main__':
	main()