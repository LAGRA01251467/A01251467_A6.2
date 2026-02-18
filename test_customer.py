import unittest
import os
from customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.file = "customers.json"
        if os.path.exists(self.file): os.remove(self.file)

    def test_create_success(self):
        self.assertTrue(Customer.create_customer("C1", "Name", "e@m.com"))

    def test_negative_duplicate(self):
        Customer.create_customer("C1", "N", "E")
        self.assertFalse(Customer.create_customer("C1", "X", "Y"))

    def test_negative_delete_none(self):
        self.assertFalse(Customer.delete_customer("999"))

    def test_negative_modify_none(self):
        self.assertFalse(Customer.modify_customer("999", name="X"))

    def test_negative_display_none(self):
        self.assertIsNone(Customer.display_customer("999"))

    def test_negative_corrupt(self):
        with open(self.file, 'w') as f: f.write("!!!")
        self.assertIsNone(Customer.display_customer("C1"))

    def test_delete_positive(self):
        Customer.create_customer("C2", "T", "t@t.com")
        self.assertTrue(Customer.delete_customer("C2"))

    def test_modify_positive(self):
        Customer.create_customer("C3", "T", "t@t.com")
        self.assertTrue(Customer.modify_customer("C3", name="New"))
