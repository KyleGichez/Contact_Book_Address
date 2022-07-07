import unittest
from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.contact = Phonebook("Kyle", "Gichez", "0716359614", "kylegichez2@gmail.com")
        result = self.contact.saveContact()
        self.assertTrue(result)
    
    def test_init(self):
        """test init"""
        self.assertEqual(self.contact.first_name, "Kyle")
        self.assertEqual(self.contact.last_name, "Gichez")
        self.assertEqual(self.contact.phone_number, "0716359614")
        self.assertEqual(self.contact.email, "kylegichez2@gmail.com")

    def tearDown(self):
        """tear down method"""
        self.contact.contacts = dict()

    def test_findContact(self):
        """test find contact by number"""
        self.assertEqual(self.contact.phone_number, "0716359614")

    def test_displayContacts(self):
        """test display all contacts"""
        contacts = Phonebook.contacts.items()
        self.assertEqual(len(contacts), 1)
    
    def test_deleteContact(self):
        """test delete contact"""
        self.contact.deleteContact("0716359614")
        contacts = Phonebook.contacts.items()
        self.assertEqual(len(contacts), 0)

if __name__ == '__main__':
    unittest.main()