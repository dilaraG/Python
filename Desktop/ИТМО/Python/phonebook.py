
from contact import Contact

class PhoneBook:
    def __init__(self, tag, is_public=True):
        self.contacts = []
        self.tag = tag
        self.is_public = is_public 

    def add_contact(self, contact):
        if not isinstance(contact, Contact):
            raise ValueError("Можно добавлять только экземпляры класса Contact.")

        self.contacts.append(contact)

    def remove_contact(self, contact):
        if contact not in self.contacts:
            raise ValueError("Контакт не найден в телефонной книжке.")
        self.contacts.remove(contact)

    def get_public_contacts(self):
        return [contact for contact in self.contacts if contact.public]

    def filter_by_country(self, country_code):
        return [contact for contact in self.contacts if contact.country_code == country_code]

    def filter_by_user(self, user):
        return [contact for contact in self.contacts if contact.user == user]
