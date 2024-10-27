from user import User, GuestUser, AdminUser, Contact

# Создаем список пользователей
users = []

# Создаем админа
admin = AdminUser("Администратор")
users.append(admin)

# Создаем гостей
guest1 = GuestUser()
guest2 = GuestUser()

# Регистрация новых пользователей
try:
    user1 = guest1.register("Алексей", users)
    user2 = guest2.register("Мария", users)
    user3 = guest1.register("Иван", users)
    user4 = guest2.register("Алина", users)
except ValueError as e:
    print(e)

# Добавляем контакты для пользователей
contact1 = Contact("Алексей", "+7917", "124567890", public=True)
contact2 = Contact("Мария", "+7936", "0987654", public=False)  # Приватный контакт
contact3 = Contact("Иван", "+7917", "7654321", public=True)
contact4 = Contact("Алина", "+7919", "1234567", public=True)

try:
    user1.add_contact(contact1, "Друзья", is_public=True)
    user2.add_contact(contact2, "Семья", is_public=False)
    user3.add_contact(contact3, "Коллеги", is_public=True)
    user4.add_contact(contact4, "Знакомые", is_public=True)
except ValueError as e:
    print(e)

# Админ добавляет дополнительный контакт любому пользователю
additional_contact = Contact("Данил", "+7919", "3456788", public=True)
admin.modify_other_user_phonebook(user2, "Семья", additional_contact, "add")  # Добавление контакта к Марии


# Гость просматривает пользователей
print("Список пользователей:", guest1.view_users(users))

# Гость просматривает публичные телефонные книжки
print("Публичные телефонные книжки:", guest1.view_public_phone_books(users))

# Админ удаляет пользователя
admin.delete_user(user3, users)  # Удаление Ивана

# Проверяем список пользователей после удаления
print("Пользователи после удаления Ивана:", [user.name for user in users])

# Попытаемся перевести одного из гостей в пользователя
admin.promote_guest_to_user(guest1, users)

# Проверяем, что у нас теперь есть новый пользователь
print("Пользователи после перевода гостя в пользователя:", [user.name for user in users])


guest = GuestUser()

# Гость просматривает пользователей
print(f'{guest.name} просматривает пользователей:')
print(guest.view_users(users))

# Гость просматривает публичные телефонные книжки
print('Гость просматривает публичные телефонные книжки:')
print(guest.view_public_phone_books(users))

# Регистрация нового пользователя
new_user = guest.register("Руслан", users)

# Гость просматривает пользователей
print(f'{guest.name} просматривает пользователей:')
print(guest.view_users(users))

# Админ добавляет контакт в телефонную книжку нового пользователя
contact = Contact("Камила", "+7917", "5764389")
new_user.add_contact(contact, "друзья", is_public=True)

# Попробуем добавить user с уже существующим именем
# guest.register("Руслан", users)

