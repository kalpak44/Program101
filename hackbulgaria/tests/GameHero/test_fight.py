from fight import Fight
from hero import Hero
from org import Org

import unittest

class TestFight(unittest.TestCase):
	def setUp(self):
		self.hero = Hero("Born", 100, "DragonSlayer")
		self.orc = Orc("Monster", 100, 2)
		self.fight = Fight(self.hero, self.orc)

	def test_init(self):
		self.assertEqual(self.hero.hero,self.hero)
		self.assertEqual(self.hero.orc,self.orc)

