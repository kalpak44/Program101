from entity import Entity
from weapon import Weapon
import unittest

class TestEntiny(unittest.TestCase):
	def setUp(self):
		self.entity = Entity("Monster", 100)

	def test_init(self):
		self.assertEqual("Monster", self.entity.name)
		self.assertEqual(100, self.entity.health)

	def test_health(self):
		self.assertEqual(100, self.entity.get_health())

	def test_take_damage(self):
		self.assertEqual(self.entity.take_damage(80),20)

	def test_take_damage_more(self):
		self.assertEqual(self.entity.take_damage(123),0)

	def test_has_weapon(self):
		self.assertFalse(self.entity.has_weapon())

	def test_equip_weapon(self):
		axe = Weapon("Axe", 25, 2)
		self.entity.equip_weapon(axe)
		self.assertEqual(self.entity.weapon, axe)

		
	def test_has_weapon_added(self):
		axe = Weapon("Axe", 25, 2)
		self.entity.equip_weapon(axe)
		self.assertTrue(self.entity.has_weapon())