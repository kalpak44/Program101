from song import Song
import json

class Playlist():
	MIN_RATING = 1
	MAX_RATING = 5

	def __init__(self, name):
		self.name = name
		self.playlist = []

	def __getitem__(self, index):
		return self.playlist[index]

	def change_playlist_name(self, name):
		self.name = name

	def add_song(self, song):
		self.playlist.append(song)

	def remove_song(self, song_title):
		for song in self.playlist:
			if song.title == song.title:
				self.playlist.remove(song)

	def total_length(self):
		total_length = 0
		for song in self.playlist:
			total_length = total_length + song.length
		return total_length

	def remove_disrated(self, rating):
		if rating < Playlist.MIN_RATING or rating > Playlist.MAX_RATING:
			raise ValueError
		else:
			for song in self.playlist:
				if song.rating <= rating:
					self.playlist.remove(song)

	def remove_bad_quality(self, bitrate):
		for song in self.playlist:
			if song.bitrate <= bitrate:
				self.playlist.remove(song)

	def show_artists(self):
		artists = []
		for song in self.playlist:
			artists.append(song.artist)
		artists = list(set(artists))
		return artists

	def save(self, filename):
		songs = [{key: song.__dict__[key] for key in song.__dict__}
		for song in self.songs]

        data = {'name': self.name, 'songs': songs}
        


def main():
	playlist = Playlist('PlayList')
	song1 = Song('title1', 'artist1', 'album1', 5, 93, 256)
	song2 = Song('title2', 'artist2', 'album2', 3, 87, 126)
	playlist.add_song(song1)
	playlist.add_song(song2)

	playlist.save('mylist')



if __name__ == '__main__':
	main()