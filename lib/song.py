class Song:
    count = 0
    genre_count = {}
    artist_count = {}

    @classmethod
    def get_genres(cls):
        return cls.genre_count.keys()

    @classmethod
    def get_artists(cls):
        return cls.artist_count.keys()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1

# Example usage:
song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")

print(Song.count)  # Output: 3
print(Song.genre_count)  # Output: {'Rap': 1, 'Pop': 1, 'Rock': 1}
print(Song.get_artists())  # Output: dict_keys(['Jay Z', 'Beyonce', 'Nirvana'])
print(Song.get_genres())  # Output: dict_keys(['Rap', 'Pop', 'Rock'])

# Unit tests
class TestSong:
    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert(out_of_touch.name == "Out of Touch")
        assert(out_of_touch.artist == "Hall and Oates")
        assert(out_of_touch.genre == "Pop")

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        assert(Song.count == 4)
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert(Song.count == 5)

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        assert("Rap" in Song.get_genres())
        assert("Pop" in Song.get_genres())
        assert("Rock" in Song.get_genres())

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        assert("Jay Z" in Song.get_artists())
        assert("Beyonce" in Song.get_artists())
        assert("Hall and Oates" in Song.get_artists())

    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        assert(Song.genre_count["Rap"] == 1)
        assert(Song.genre_count["Pop"] == 3)
        assert(Song.genre_count["Rock"] == 1)

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        assert(Song.artist_count["Jay Z"] == 1)
        assert(Song.artist_count["Beyonce"] == 1)
        assert(Song.artist_count["Nirvana"] == 1)
        assert(Song.artist_count["Hall and Oates"] == 2)

# Run the unit tests
test = TestSong()
test.test_saves_name_artist_genre()
test.test_has_song_count()
test.test_has_genres()
test.test_has_artists()
test.test_has_genre_count()
test.test_has_artist_count()