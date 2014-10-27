class Song():
	MIN_RATING = 1
	MAX_RATING = 5
	def __init__(self, title, artist, album, rating, length, bitrate):
		self.title = title
		self.artist =  artist
		self.album = album
		self.rating = rating
		self.length = length
		self.bitrate = bitrate

	def rate(self, rating):
		if rating > Song.MIN_RATING and rating < Song.MAX_RATING:
			self.rating = rating
		else:
			raise ValueError