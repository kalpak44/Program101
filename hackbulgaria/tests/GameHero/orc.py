from entity import Entity

class Orc(Entity):
	def __init__(self, name, health, nickname):
		super().__init__(name, health)

	def __init__(self, name, health, berserk_factor):
		self.name = name
		self.health = health
		self.set_bf(berserk_factor)
		
		self.MAX_HEALTH = 100

	def set_bf(self, berserk_factor):
		if berserk_factor > 2 or berserk_factor < 1:
			raise ValueError
		else:
			self.berserk_factor = berserk_factor

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