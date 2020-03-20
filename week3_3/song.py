from utils import parse_length

class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.hours, self.minutes, self.seconds = parse_length(length)

    def __str__(self):
        if self.hours == 0:
            return f"{self.artist} - {self.title} from {self.album} - {self.minutes}:{self.seconds}" 
        return f"{self.artist} - {self.title} from {self.album} - {self.hours}:{self.minutes}:{self.seconds}"

    def __eq__(self, other):
        if (self.title == other.title and self.artist == other.artist
        and self.album == other.album and self.hours == other.hours
        and self.minutes == other.minutes and self.seconds == other.seconds):
            return True
        return False

    def __hash__(self):
        return hash((self.title,self.artist))

    def length(self, seconds = False, minutes = False, hours = False):
        if seconds:
            return self.seconds
        elif minutes:
            return self.minutes
        elif hours:
            return self.hours
        else:
            if self.hours == 0:
                return f"{self.minutes}:{self.seconds}"
            return f"{self.hours}:{self.minutes}:{self.seconds}"