import unittest
from song import Song

class TestSong(unittest.TestCase):
    def test_initialization(self):
        title = "Odin"
        artist = "Manowar"
        album = "The Sons of Odin"
        length = "3:44"

        song = Song(title, artist, album, length)

        self.assertEqual(title,song.title)
        self.assertEqual(artist,song.artist)
        self.assertEqual(album,song.album)

    def test_printing(self):
        title = "Odin"
        artist = "Manowar"
        album = "The Sons of Odin"
        length_with_hours = "5:3:44" 
        length_without_hours = "3:44"

        song = Song(title, artist, album, length_with_hours)
        song2 = Song(title, artist, album, length_without_hours)

        self.assertEqual(f"{artist} - {title} from {album} - {length_with_hours}",str(song))
        self.assertEqual(f"{artist} - {title} from {album} - {length_without_hours}",str(song2))

    def test_equality(self):
        song = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "3:44")        
        song_different = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "3:45")        
        song_equal = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = "3:44")        

        self.assertTrue(song == song_equal)
        self.assertFalse(song == song_different)

    def test_length(self):
        length_with_hours = "8:3:44"
        length_without_hours = "8:44"
        song = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = length_with_hours)        
        song2 = Song(title = "Odin", artist = "Manowar", album = "The Sons of Odin", length = length_without_hours)        

        result_seconds = song.length(seconds = True)
        result_minutes = song.length(minutes = True)
        result_hours = song.length(hours = True)
        result_string_song = song.length()
        result_string_song2 = song2.length()

        self.assertEqual(44,result_seconds)
        self.assertEqual(3,result_minutes)
        self.assertEqual(8,result_hours)
        self.assertEqual(length_with_hours,result_string_song)
        self.assertEqual(length_without_hours,result_string_song2)

if __name__ == '__main__':
    unittest.main()