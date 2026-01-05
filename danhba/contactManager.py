class ContactManager:
    def __init__(self):
        self.contacts = []
    def addContact(self, contact):
        self.contacts.append(contact)
    def deleteContact(self, contact):
        self.contacts.remove(contact)
    def findContact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        print("No such contact.")
    def changeContactName(self, name, newName):
        for contact in self.contacts:
            if contact.name == name:
                contact.name = newName
                return contact
    def changeContactEmail(self, email, newEmail):
        for contact in self.contacts:
            if contact.email == email:
                contact.email = newEmail
                return contact
    def changeContactPhone(self, phone, newPhone):
        for contact in self.contacts:
            if contact.phone == phone:
                contact.phone = newPhone
                return contact
    def printContacts(self):
        for contact in self.contacts:
            print(contact)
