class Item:
    def __init__(self, quantity_req=0, quantity_res=0, name=""):
        self._quantity_req = quantity_req
        self._quantity_res = quantity_res
        self._name = name

    @property
    def quantity_req(self):
        return self._quantity_req

    @property
    def quantity_res(self):
        return self._quantity_res

    @property
    def name(self):
        return self._name
    

    @quantity_req.setter
    def quantity_req(self, value):
        if (value<0):
            raise ValueError("value must be non-negative")
        self._quantity_req = value

    @quantity_res.setter
    def quantity_res(self, value):
        if (value<0):
            raise ValueError("value must be non-negative")
        self._quantity_res = value

    @name.setter
    def name(self, value):
        self._name = value

