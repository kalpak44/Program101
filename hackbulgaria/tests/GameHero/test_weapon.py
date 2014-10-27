from weapon import Weapon
import unittest

class TestWeapon(unittest.TestCase):
	def setUp(self):
		self.axe = Weapon("axe", 12, 1)

	def test_init(self):
		self.assertEqual("axe", self.axe.type)
		self.assertEqual(12, self.axe.damage)
		self.assertEqual(1, self.axe.critical_strike_percent)

	def test_critical_hit_one(self):
		self.axe.critical_strike_percent = 1
		self.assertFalse(self.axe.critical_hit())

	def test_critical_hit_two(self):
		self.axe.critical_strike_percent = 2
		self.assertTrue(self.axe.critical_hit())

	def test_critical_hit_other(self):
		self.axe.critical_strike_percent = 13
		self.assertFalse(self.axe.critical_hit())