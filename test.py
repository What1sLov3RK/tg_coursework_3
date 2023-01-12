from main import *
import requests
import unittest

class TestFindSongByTitle(unittest.TestCase):
    def test_find_song_by_title(self):
        # Test that the function returns the correct video URL and song title for a known search query
        title = "Shape of You"
        print("title = " + title)
        expected_url = "https://www.youtube.com/watch?v=JGwWNGJdvx8"
        expected_name = "Ed Sheeran - Shape of You (Official Music Video)"
        print("expected name = " + expected_name)
        print("expected url = " + expected_url)

        result, name = find_song_by_title(title)
        print("Url = " + result)
        print(self.assertEqual(result, expected_url))
        print(self.assertEqual(name, expected_name))

    def test_find_song_by_title_invalid_input(self):
        # Test that the function raises an error when given invalid input
        title = ""
        print(self.assertRaises(ValueError, find_song_by_title, title))


class TestFindSongByLyrics(unittest.TestCase):
    def test_find_song_by_lyrics(self):
        # Test that the function returns the correct video URL and song title for a known search query
        lyrics = "I am in love with a shape of you"
        print("lyrics = " + lyrics)
        expected_url = "https://www.youtube.com/watch?v=JGwWNGJdvx8"
        expected_name = "Ed Sheeran - Shape of You (Official Music Video)"
        print("expected name = " + expected_name)
        print("expected url = " + expected_url)
        result, name = find_song_by_title(lyrics)
        print("Url = " + result)
        print(self.assertEqual(result, expected_url))
        print(self.assertEqual(name, expected_name))

    def test_find_song_by_title_invalid_input(self):
        # Test that the function raises an error when given invalid input
        lyrics = ""
        print(self.assertRaises(ValueError, find_song_by_title, lyrics))

if  __name__  == 'main':
    unittest.main()