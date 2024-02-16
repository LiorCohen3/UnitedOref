from enum import Enum
import Location
import Item
import Date

class Status(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class Request:
    def __init__(self, request_number, Status, location:Location, area, info, req_unit, donor, receiver, date :Date, items: Item=[]):
        self.request_number = request_number
        self.status = Status
        self.location = location
        self.area = area
        self.info = info
        self.req_unit = req_unit
        self.items = items
        self.donor = donor
        self.receiver = receiver
        self.date = date

    @property
    def request_number(self):
        return self._request_number

    @property
    def status(self):
        return self._status

    @property
    def location(self):
        return self._location

    @property
    def area(self):
        return self._area

    @property
    def info(self):
        return self._info

    @property
    def req_unit(self):
        return self._req_unit

    @property
    def items(self):
        return self._items

    @property
    def donor(self):
        return self._donor

    @property
    def receiver(self):
        return self._receiver

    @property
    def time_and_date(self):
        return self._time_and_date