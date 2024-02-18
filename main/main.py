from Date import Date
from Item import Item 
from Location import Location
from Request import Request
from Request import Status
from datetime import datetime


wqe = Item (10,1,"shit")
itemList=[wqe,wqe,wqe]
time=Date("yes")
loc=Location(0,0)
donation="" #???????
request = Request(1,Status.Done,loc,"North","info",669,"donor","receiver",time,itemList)
request2 = Request(2,Status.Done,loc,"North","info",669,"donor","receiver",time,itemList)
request3 = Request(3,Status.Done,loc,"North","info",669,"donor","receiver",time,itemList)
requests=[request,request2,request3,] #pull db

current_date_time = datetime.now()
formatted_year = current_date_time.strftime("%y")
formatted_month = current_date_time.strftime("%m")
formatted_day=current_date_time.strftime("%d")

for i in requests:
    for j in i.items:
        if(j.quantity_res>0):
            i.algScore+=10
    i.algScore=i.algScore*(i.request_number/100)
    print(i.algScore)
    
    
            
           
        
