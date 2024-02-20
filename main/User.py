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
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @email.setter
    def email(self, value):
        self._email = value

    @password.setter
    def password(self, value):
        self._password = value

    @unit.setter
    def unit(self, value):
        self._unit = value

    @requests.setter
    def requests(self, value):
        self._requests = value
