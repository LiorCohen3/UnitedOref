class User:
    def __init__(self, first_name, last_name, phone_number, email, password, unit, requests=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.unit = unit
        self.requests = requests

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def unit(self):
        return self._unit

    @property
    def requests(self):
        return self._requests