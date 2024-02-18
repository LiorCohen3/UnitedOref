class User:
    def __init__(self, first_name, last_name, phone_number, email, password, unit, requests=[]):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._email = email
        self._password = password
        self._unit = unit
        self._requests = requests

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