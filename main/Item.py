class Item:
    def __init__(self,itemType, quantityReq=0 , name=""):
        self._itemType = itemType
        self._quantity_req = quantityReq
        self._name = name

    @property
    def itemType(self):
        return self._itemType
    
    @property
    def quantityReq(self):
        return self._quantityReq

    @property
    def name(self):
        return self._name
    
    @itemType.setter
    def itemType(self, value):
        if (value!=1|value!=0):
            raise ValueError("value must be valid type")
        self._itemType = value

    @quantityReq.setter
    def quantityReq(self, value):
        if (value<0):
            raise ValueError("value must be non-negative")
        self._quantityReq = value

    @name.setter
    def name(self, value):
        self._name = value