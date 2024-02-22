class Date:
    def __init__(self, time, day=1 ,month=1, year=2024):
        self._time = time
        self._day = day
        self._month = month
        self._year = year

    @property
    def time(self):
        return self._time
    
    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    @time.setter
    def time(self, value):
        self._time = value

    @day.setter
    def day(self, value):
        self._day = value

    @month.setter
    def month(self, value):
        self._month = value

    @year.setter
    def year(self, value):
        self._year = value