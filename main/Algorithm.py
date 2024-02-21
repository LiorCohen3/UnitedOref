# from Date import Date
# from Item import Item 
# from Location import Location
# from Request import Request
# from Request import Status
import models 

# area 1-north  2-center  3-south
# type 1-food  2-equ
# autoMatch 1-auto  2-manual

#donationCap=20

def alg(requests,area="North",type=1,autoMatch=True): 
    for index,request in requests:
        if request.area == area:  #same area donation
            request.algScore+=10
        elif (area=="North"&request.area=="South")|(area=="South"&request.area=="North"):   #far area donation
            request.algScore+=1
        else:   #semi far area donation
            request.algScore+=5

        if request.type_id==type: #type of donation matchs
            request.algScore+=10
        # if request.type_id.quantityReq<=donationCap:    #he can donate more then the req
        #     request.algScore+=5*(donationCap/request.type_id.quantityReq)
        # else:   #the amount he can is lower then the req
        #     request.algScore-=30

        request.algScore+=(10/(index+1))    #add score by the index for the request

    sorted_list = sorted(requests, key=lambda x: x.algScore, reverse=True) #order list by highest algScore

    if autoMatch:
        return sorted_list[0] #return requset with highest score
        
    else:
        return sorted_list  #return all the requests
        