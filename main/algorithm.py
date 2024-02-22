# from Date import Date
# from Item import Item 
# from Location import Location
# from Request import Request
# from Request import Status
from datetime import datetime

# import models


# area 1-north  2-center  3-south
# type 1-food  2-equ
# auto_match 1-auto  2-manual

# donationCap=20


def alg(requests_list, auto_match: bool, area, item_type, donation_type=1):
    alg_score = {}
    current_date_time = datetime.now()
    current_year = current_date_time.year
    current_month = current_date_time.month
    current_day = current_date_time.day
    for index, req in enumerate(requests_list):
        alg_score[index] = 1
        if req.area == area:  # same area donation
            alg_score[index] = alg_score[index] + 200
        elif (area == "North" and req.area == "South") or (
                area == "South" and req.area == "North"):  # far area donation
            alg_score[index] = alg_score[index] + 10
        else:  # semi far area donation
            alg_score[index] = alg_score[index] + 100

        if req.type_id == int(item_type):  # type of donation matchs
            alg_score[index] = alg_score[index] + 200
        # if request.type_id.quantityReq<=donationCap:    #he can donate more then the req
        #     alg_score[index]+=5*(donationCap/request.type_id.quantityReq)
        # else:   #the amount he can is lower then the req
        #     alg_score[index]-=30

        request_date = str(req.date).split('-')
        request_year = int(request_date[0])
        request_month = int(request_date[1])
        request_day = int(request_date[2])

        current_date = datetime(current_year, current_month, current_day)
        request_date = datetime(request_year, request_month, request_day)
        difference = current_date - request_date
        diff_days = difference.days if difference.days < 180 else 180  # 180 days is the maximum to be scored
        alg_score[index] += (2 * diff_days)

    sorted_keys = list(sorted(alg_score, key=lambda x: alg_score[x], reverse=True))
    sorted_requests = [requests_list[i] for i in sorted_keys]
    if auto_match:
        return [sorted_requests[0]]  # return request with the highest score

    else:
        return sorted_requests  # return all the requests
