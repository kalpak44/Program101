from song import Song
import unittest
class Tests(unittest.TestCase):
	def setUp(self):
		self.song = Song('title', 'artist', 'album', 5, 93, 256)

	def test_song_init(self):
		song = Song('title', 'artist', 'album', 5, 93, 256)
		self.assertEqual(song.title, 'title')
		self.assertEqual(song.artist, 'artist')
		self.assertEqual(song.album, 'album')
		self.assertEqual(song.rating,5)
		self.assertEqual(song.length, 93)
		self.assertEqual(song.bitrate, 256)
		
	def test_rate(self):
		self.song.rate(3)
		self.assertEqual(self.song.rating, 3)


	def test_rate_out_range(self):
		with self.assertRaises(ValueError):
			self.song.rate(200)



if __name__ == '__main__':
	main()