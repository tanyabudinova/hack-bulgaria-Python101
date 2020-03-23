import random
from song import Song
from utils import total_length_helper

class Playlist:
    def __init__(self, name, repeat = False, shuffle = False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist = []
        self.indices = None

    def add_song(self, song):
        self.playlist.append(song)
        if self.indices != None:
            self.indices.append(len(self.playlist) - 1)

    def remove_song(self, song):
        try:
            idx = self.playlist.index(song)
            self.playlist.remove(song)
            self.indices = list(map(lambda x: x - 1 if x > idx else x, self.indices))
            self.indices.remove(idx)            
        except:
            pass

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        seconds = 0
        minutes = 0
        hours = 0
        seconds, minutes = total_length_helper(seconds, minutes, self.playlist, lambda x: x.length(seconds = True))
        minutes, hours = total_length_helper(minutes, hours, self.playlist, lambda x: x.length(minutes = True))

        hours += sum(list(map(lambda x: x.length(hours = True), self.playlist)))

        if hours == 0:
            return f"{minutes}:{seconds}"
        return f"{hours}:{minutes}:{seconds}"

    def next_song(self):
        if self.indices == None:
            self.indices = list(range(len(self.playlist)))
        if self.indices == []:
            if self.repeat == True:
                self.indices = list(range(len(self.playlist)))
            else:    
                raise ValueError("The playlist ended")
        if self.shuffle == True:
            next_song_idx = random.choice(self.indices)
            self.indices.remove(next_song_idx)
            return self.playlist[next_song_idx]
        else:
            next_song_idx = self.indices[0]
            self.indices.remove(next_song_idx)
            return self.playlist[next_song_idx]




