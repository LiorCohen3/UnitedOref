class Date:
    def __init__(self, time, month=1, day=1, year=2024):
        self._time = time
        self._month = month
        self._day = day
        self._year = year

    @property
    def time(self):
        return self._time

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def year(self):
        return self._year