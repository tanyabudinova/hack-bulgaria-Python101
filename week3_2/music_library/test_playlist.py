import unittest
from playlist import Playlist
from song import Song

class TestPlaylist(unittest.TestCase):
    def test_total_length_without_hours(self):
        s = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "3:44")
        playlist = Playlist(name = "Code")
        playlist.add_song(s)
        playlist.add_song(s)
        playlist.add_song(s)

        result = playlist.total_length()

        self.assertEqual("11:12", result)

    def test_total_length_with_hours(self):
        s = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "1:33:44")
        playlist = Playlist(name = "Code")
        playlist.add_song(s)
        playlist.add_song(s)
        playlist.add_song(s)

        result = playlist.total_length()

        self.assertEqual("4:41:12", result)

    def test_next_song_at_the_last_song_wihtout_repeat(self):
        s = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "3:44")
        playlist = Playlist(name = "Code")
        playlist.add_song(s)

        song = playlist.next_song()
        exc = None

        try:
            playlist.next_song()
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual("The playlist ended", str(exc))

    def test_next_song_at_the_last_song_wiht_repeat(self):
        s = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "3:44")
        playlist = Playlist(name = "Code",repeat = True)
        playlist.add_song(s)

        song = playlist.next_song()
        song = playlist.next_song()

        self.assertEqual(s, song)

    def test_next_song_with_shuffle_does_not_repeat_song_until_all_are_played(self):
        s = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "3:44")
        s2 = Song(title = "Odin", artist = "Manowar", album = "The Sons of Toni", length = "3:44")
        playlist = Playlist(name = "Code",shuffle = True)
        playlist.add_song(s)
        playlist.add_song(s2)

        song = playlist.next_song()
        song2 = playlist.next_song()

        self.assertFalse(song == song2)

    def test_remove_song_while_at_shuffle(self):
        s = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "3:44")
        playlist = Playlist(name = "Code",shuffle = True)
        playlist.add_song(s)
        playlist.add_song(s)
        playlist.add_song(s)
        
        song = playlist.next_song()
        playlist.remove_song(s)
        song = playlist.next_song()
        exc = None
        try:
            playlist.next_song()
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual("The playlist ended", str(exc))

    def test_add_song_while_at_shuffle(self):
        s = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "3:44")
        playlist = Playlist(name = "Code",shuffle = True)
        playlist.add_song(s)
        playlist.add_song(s)
        
        song = playlist.next_song()
        playlist.add_song(s)
        song1 = playlist.next_song()
        song2 = playlist.next_song()

if __name__ == '__main__':
    unittest.main()