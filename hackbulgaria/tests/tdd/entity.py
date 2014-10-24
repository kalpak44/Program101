class Entity:
	def __init__(self, name, health):
		self.name = name
		self.health = health

		self.MAX_HEALTH = 100
		self.weapon = None

	def get_health(self):
		return self.health

	def is_alive(self):
		if self.health > 0:
			return True
		else:
			return False

	def take_damage(self, damage_points):
		if self.health < damage_points:
			self.health = 0
			return self.health
		else:
			return self.health - damage_points

	def take_healing(self, healing_points):
		if self.health == 0:
			return False
		else:
			health = self.health + healing_points
			if health > self.MAX_HEALTH:
				self.health = self.MAX_HEALTH
			else:
				self.health = health
			return True

	def has_weapon(self):
		if self.weapon != None:
			return True
		else:
			return False

	def equip_weapon(self, weapon):
		self.weapon = weapon