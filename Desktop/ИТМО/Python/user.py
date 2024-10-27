
from phonebook import PhoneBook
from contact import Contact

class User:
    def __init__(self, name):
        self.name = name
        self.friends = set()
        self.phone_books = {}

    def add_contact(self, contact, tag, is_public=True):
        if tag not in self.phone_books:
            self.phone_books[tag] = PhoneBook(tag, is_public)
        self.phone_books[tag].add_contact(contact)

    def share(self, friend, tag):
        if friend not in self.friends:
            raise ValueError(f"{friend.name} не является другом.")
        if tag not in self.phone_books:
            raise ValueError(f"Телефонная книжка с тегом '{tag}' не найдена.")

        if not self.phone_books[tag].is_public:
            raise PermissionError("Эта телефонная книжка является приватной.")

        shared_contacts = self.phone_books[tag].get_public_contacts()
        return f"{self.name} поделился контактами из '{tag}' с {friend.name}: {shared_contacts}"

    def add_friend(self, friend):
        self.friends.add(friend)

    def remove_friend(self, friend):
        self.friends.discard(friend)

class GuestUser:
    def __init__(self):
        self.name = "Гость"

    def view_users(self, users):
        return [user.name for user in users]

    def view_public_phone_books(self, users):
        public_books = {}
        for user in users:
            for tag, phone_book in user.phone_books.items():
                if phone_book.is_public:
                    public_books[tag] = phone_book.get_public_contacts()
        return public_books

    def register(self, name, users):
        if any(user.name == name for user in users):
            raise ValueError("Пользователь с таким именем уже существует.")
        new_user = User(name)
        users.append(new_user)
        return new_user

class AdminUser(User):
    def delete_user(self, user_to_delete, users):
        if user_to_delete not in users:
            raise ValueError("Пользователь не найден.")
        users.remove(user_to_delete)

    def promote_guest_to_user(self, guest_user, users):
        if guest_user.name in [user.name for user in users]:
            raise ValueError("Пользователь с таким именем уже существует.")
        new_user = User(guest_user.name)
        users.append(new_user)

    def modify_other_user_phonebook(self, other_user, tag, new_contact, action):
        if tag not in other_user.phone_books:
            raise ValueError(f"Телефонная книжка с тегом '{tag}' не найдена у пользователя {other_user.name}.")
        if action == "add":
            other_user.phone_books[tag].add_contact(new_contact)
        elif action == "remove":
            other_user.phone_books[tag].remove_contact(new_contact)
        else:
            raise ValueError("Недопустимое действие. Используйте 'add' или 'remove'.")
