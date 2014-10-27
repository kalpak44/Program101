from playlist import Playlist
from song import Song

import unittest
class Tests(unittest.TestCase):
	def setUp(self):
		self.playlist = Playlist('PlayList')
		self.song = Song('title', 'artist', 'album', 5, 93, 256)

	def test_song_init(self):
		self.assertEqual(self.playlist.name, 'PlayList')

	def test_add_song(self):
		self.playlist.add_song(self.song)
		self.assertEqual(self.playlist.playlist[0],self.song)

	def test_remove_song(self):
		self.playlist.remove_song('title')
		self.assertEqual(len(self.playlist.playlist), 0)

	def test_total_length(self):
		song1 = Song('title1', 'artist1', 'album1', 5, 93, 256)
		song2 = Song('title2', 'artist2', 'album2', 3, 87, 126)
		self.playlist.add_song(song1)
		self.playlist.add_song(song2)
		self.assertEqual(self.playlist.total_length(),180)

	def test_remove_disrated(self):
		song1 = Song('title1', 'artist1', 'album1', 5, 93, 256)
		song2 = Song('title2', 'artist2', 'album2', 3, 87, 126)
		song3 = Song('title3', 'artist3', 'album3', 5, 88, 148)
		self.playlist.add_song(song1)
		self.playlist.add_song(song2)
		self.playlist.add_song(song3)
		self.playlist.remove_disrated(3)
		self.assertEqual(self.playlist.total_length(),181)

	def test_remove_bad_quality(self):
		song1 = Song('title1', 'artist1', 'album1', 5, 93, 256)
		song2 = Song('title2', 'artist2', 'album2', 3, 87, 126)
		song3 = Song('title3', 'artist3', 'album3', 5, 88, 148)
		self.playlist.add_song(song1)
		self.playlist.add_song(song2)
		self.playlist.add_song(song3)
		self.playlist.remove_bad_quality(126)
		self.assertEqual(self.playlist.total_length(),181)

	def test_show_artists(self):
		song1 = Song('title1', 'artist1', 'album1', 5, 93, 256)
		song2 = Song('title2', 'artist2', 'album2', 3, 87, 126)
		song3 = Song('title3', 'artist2', 'album3', 5, 88, 148)
		self.playlist.add_song(song1)
		self.playlist.add_song(song2)
		self.playlist.add_song(song3)
		artists = ['artist1','artist2']
		self.assertEqual(artists,self.playlist.show_artists())

	def test_str(self):
		song1 = Song('title1', 'artist1', 'album1', 5, 93, 256)
		song2 = Song('title2', 'artist2', 'album2', 3, 87, 126)
		self.playlist.add_song(song1)
		self.playlist.add_song(song2)
		songs = 'artist1 title1 - 1:33\nartist2 title2 - 1:27\n'
		self.assertEqual(songs,self.playlist.str())






if __name__ == '__main__':
	main()