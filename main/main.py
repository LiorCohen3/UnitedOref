from Date import Date
from Item import Item 
from Location import Location
from Request import Request
from Request import Status

hash_table = {
    1: 'North',
    2: 'Center',
    3: 'South'
}

sentItem=Item (1,10,"shit")
time=Date("yes")
loc=Location(0,0)
donationArea=1 # 1-north  2-center  3-south
donationType=1 # 1-food  2-equ
donationAlg=1 # 1-auto  2-manual
request1 = Request(1,Status.Done,loc,1,"info",669,"donor","receiver",time,sentItem)
request2 = Request(2,Status.Done,loc,2,"info",669,"donor","receiver",time,sentItem)
request3 = Request(3,Status.Done,loc,3,"info",669,"donor","receiver",time,sentItem)
requests=[request1,request2,request3,] #pull db

#number of items in the request
# 1-done 2-pending 3-not delivered

# time, order by fifo add to alg
# item amount to donate and the type in auto alg

def alg(area,type,alg):  #need to add item type, area, auto/manual
    for i in requests:
        if i.area== area:  #same area donation
            i.algScore+=10
        elif i.area-area==1:   #semi far area donation
            i.algScore+=5
        else:   #far area donation
            i.algScore+=1
        print("in area "+hash_table.get(i.area),i.algScore)

        if i.item.itemType==type:
            i.algScore+=10
        else:
            i.algScore+=5
        print("type is worth",i.algScore)

#       need to add a score system for time
# 
#       need to add a score system for food requested and what he can donate 50/30
# 
        
    if alg==1:
        #return requests with highest score
        print()
    else:
        #return all the
        print()

alg(donationArea,donationType,donationAlg)