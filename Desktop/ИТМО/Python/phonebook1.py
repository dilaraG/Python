
class Contact:
    def __init__(self, user, country_code, phone_number):
        self.user = user
        self.country_code = country_code
        self.phone_number = phone_number

    def __repr__(self):
        return f"{self.user}'s contact: {self.phone_number} ({self.country_code})"

class PhoneBook:
    def __init__(self, tag):
        self.contacts = []
        self.tag = tag

    def add_contact(self, contact):
        if not isinstance(contact, Contact):
            raise ValueError("Можно добавлять только экземпляры класса Contact.")
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def filter_by_country(self, country_code):
        return [contact for contact in self.contacts if contact.country_code == country_code]

    def filter_by_user(self, user):
        return [contact for contact in self.contacts if contact.user == user]


class User:
    def __init__(self, name):
        self.name = name
        self.friends = set()
        self.phone_books = {}

    def add_contact(self, contact, tag):
        if tag not in self.phone_books:
            self.phone_books[tag] = PhoneBook(tag)
        self.phone_books[tag].add_contact(contact)

    def share(self, friend, tag):
        if friend not in self.friends:
            raise ValueError(f"{friend.name} не является другом.")
        if tag not in self.phone_books:
            raise ValueError(f"Телефонная книжка с тегом '{tag}' не найдена.")
        
        shared_contacts = self.phone_books[tag].contacts
        return f"{self.name} поделился контактами из '{tag}' с пользователем {friend.name}: {shared_contacts}"

    def add_friend(self, friend):
        self.friends.add(friend)

    def remove_friend(self, friend):
        self.friends.discard(friend)


user1 = User("Алиса")
user2 = User("Тимур")

# Добавление друзей
user1.add_friend(user2)

# Добавление контактов
contact1 = Contact("мама", "+1", "1234567890")
user1.add_contact(contact1, "семья")

# Делимся контактами
try:
    print(user1.share(user2, "семья"))  
    print(user1.share(User("Мария"), "семья")) 
except ValueError as e:
    print(e)
