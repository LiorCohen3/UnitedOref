import Date
import Item
import Location
import Request

wqe = Item.Item (1,0,"shit")
asd=[wqe]
time=Date.Date("yes")
loc=Location.Location(0,0)

request = (1,Request.Status,loc,"North","hello there",669,"sad","sad",time,asd)

print(request)