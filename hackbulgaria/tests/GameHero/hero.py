from entity import Entity

class Hero(Entity):
	def __init__(self, name, health, nickname):
		super().__init__(name, health)

	def __init__(self, name, health, nickname):
		self.name = name
		self.health = health
		self.nickname = nickname
		self.MAX_HEALTH = 100

	def known_as(self):
		return "{} the {}".format(self.name, self.nickname)

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