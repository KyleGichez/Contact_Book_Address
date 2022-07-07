class Phonebook:
    contacts = dict()

    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def saveContact(self):
        self.contacts[self.phone_number] = self
        return self or None

    @classmethod
    def findContact(cls, number):
       return cls.contacts.get(number)

    @classmethod
    def displayContacts(cls):
        return cls.contacts.items()
    
    @classmethod
    def deleteContact(cls, number):
        cls.contacts.pop(number)
        return True
