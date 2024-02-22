class Location:
    def __init__(self, longitude=0, latitude=0):
        self._longitude = longitude
        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude