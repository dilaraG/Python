class Contact:
    def __init__(self, user, country_code, phone_number, public=True):
        self.user = user
        self.country_code = country_code
        self.phone_number = phone_number
        self.public = public 

    def __repr__(self):
        return f"{self.user} контакт: ({self.country_code}) {self.phone_number} "