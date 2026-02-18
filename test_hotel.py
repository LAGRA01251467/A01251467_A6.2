import unittest
import os
from hotel import Hotel

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.file = "hotels.json"
        if os.path.exists(self.file): os.remove(self.file)

    def test_create_and_display(self):
        Hotel.create_hotel("H1", "Hotel Test", "Loc", 10)
        self.assertEqual(Hotel.display_hotel("H1")['name'], "Hotel Test")

    def test_negative_duplicate(self):
        Hotel.create_hotel("H1", "H", "L", 5)
        self.assertFalse(Hotel.create_hotel("H1", "Other", "L", 5))

    def test_negative_delete_none(self):
        self.assertFalse(Hotel.delete_hotel("999"))

    def test_negative_modify_none(self):
        self.assertFalse(Hotel.modify_hotel("999", name="None"))

    def test_negative_display_none(self):
        self.assertIsNone(Hotel.display_hotel("999"))

    def test_negative_corrupt_file(self):
        with open(self.file, 'w') as f: f.write("invalid")
        self.assertIsNone(Hotel.display_hotel("H1"))

    def test_modify_positive(self):
        Hotel.create_hotel("H1", "H", "L", 5)
        self.assertTrue(Hotel.modify_hotel("H1", name="New"))

    def test_delete_positive(self):
        Hotel.create_hotel("H1", "H", "L", 5)
        self.assertTrue(Hotel.delete_hotel("H1"))
