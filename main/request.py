from enum import Enum
from item import Item
from location import Location
from date import Date


class RequestStatusId(Enum):
    DONE = 1
    PENDING = 2
    NOT_DELIVERED = 3


class Request:
    def __init__(self, request_number, donation_status: RequestStatusId, location: Location, area, info, req_unit, donor,
                 receiver, req_date: Date, item: Item):
        self._request_number = request_number
        self._donation_status = donation_status
        self._location = location
        self._area = area
        self._info = info
        self._req_unit = req_unit
        self._item = item
        self._donor = donor
        self._receiver = receiver
        self._req_date = req_date
        self._algScore = 1

    @property
    def request_number(self):
        return self._request_number

    @property
    def donation_status(self):
        return self._donation_status

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
    def item(self):
        return self._item

    @property
    def donor(self):
        return self._donor

    @property
    def receiver(self):
        return self._receiver

    @property
    def req_date(self):
        return self._req_date

    @property
    def algScore(self):
        return self._algScore

    @request_number.setter
    def request_number(self, value):
        if value < 0:
            raise ValueError("value must be non-negative")
        self._request_number = value

    @donation_status.setter
    def donation_status(self, value):
        if value != type(RequestStatusId):
            raise ValueError("value must be valid Status")
        self._donation_status = value

    @location.setter
    def location(self, value):
        if value != type(Location):
            raise ValueError("value must be valid location")
        self._location = value

    @area.setter
    def area(self, value):
        self._area = value

    @req_unit.setter
    def req_unit(self, value):
        self.req_unit = value

    @info.setter
    def info(self, value):
        self._info = value

    @req_unit.setter
    def req_unit(self, value):
        self._req_unit = value

    @item.setter
    def item(self, value):
        if value != type(Item):
            raise ValueError("value must be valid location")
        self._item = value

    @donor.setter
    def donor(self, value):
        self._donor = value

    @receiver.setter
    def receiver(self, value):
        self._receiver = value

    @req_date.setter
    def req_date(self, value):
        if value != type(Date):
            raise ValueError("value must be valid date")
        self._req_date = value

    @algScore.setter
    def algScore(self, value):
        if value < 0:
            raise ValueError("value must be non-negative")
        self._algScore = value
