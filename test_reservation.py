import unittest
import os
from reservation import Reservation

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.file = "reservations.json"
        if os.path.exists(self.file): os.remove(self.file)

    def test_create_cancel(self):
        Reservation.create_reservation("R1", "C1", "H1")
        self.assertTrue(Reservation.cancel_reservation("R1"))

    def test_negative_cancel_none(self):
        self.assertFalse(Reservation.cancel_reservation("999"))

    def test_negative_corrupt(self):
        with open(self.file, 'w') as f: f.write("error")
        self.assertFalse(Reservation.cancel_reservation("R1"))

    def test_to_dict(self):
        r = Reservation("R1", "C1", "H1")
        self.assertEqual(r.to_dict()['res_id'], "R1")

    def test_load_error(self):
        with open(self.file, 'w') as f: f.write("error")
        self.assertEqual(Reservation._load_data(), [])
