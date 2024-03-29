from datetime import datetime


def alg(requests_list, area, item_type, count, donation_type):
    alg_score = {}
    for index, req in enumerate(requests_list):
        alg_score[index] = 0
        if req.area == area:  # same area donation
            alg_score[index] = alg_score[index] + 200
        elif (area == "North" and req.area == "South") or (
                area == "South" and req.area == "North"):  # far area donation
            alg_score[index] = alg_score[index] + 10
        else:  # semi far area donation
            alg_score[index] = alg_score[index] + 100

        if req.item_type.item_type_id == int(item_type):  # type of item matches
            alg_score[index] += 150
            if req.item_quantity <= count:  # he can donate more than the req
                alg_score[index] += 50 * (req.item_quantity / count)
            else:  # the amount he can is lower than the req
                alg_score[index] -= 40
        if req.type_id == int(donation_type):
            alg_score[index] += 100

        alg_score[index] -= req.requestor.donations_received * 5  # take into account completed requestor donations

        current_date = datetime.now()

        schedule_date = str(req.schedule_date).split('-')
        schedule_year = int(schedule_date[0])
        schedule_month = int(schedule_date[1])
        schedule_day = int(schedule_date[2])
        schedule_date = datetime(schedule_year, schedule_month, schedule_day)

        if current_date > schedule_date:  # if the scheduled time for the request has already passed
            request_date = str(req.date).split('-')
            request_year = int(request_date[0])
            request_month = int(request_date[1])
            request_day = int(request_date[2])
            request_date = datetime(request_year, request_month, request_day)

            difference = current_date - request_date
            diff_days = difference.days if difference.days < 180 else 180  # 180 days is the maximum to be scored
            alg_score[index] += (2 * diff_days)

        else:
            print(f"schedule_date: {schedule_date}")
            difference = schedule_date - current_date
            diff_days = difference.days
            score_by_days = 180 - diff_days if diff_days < 180 else 0  # 180 days is the maximum to be scored
            #  the score is based on how close the scheduled date is, the smaller the difference the higher the score
            alg_score[index] += (2 * score_by_days)

        print(f"req_id: {req.requests_id} area: {req.area} item_type: {req.item_type} type_id: {req.type_id}"
              f" score: {alg_score[index]}")

    sorted_keys = list(sorted(alg_score, key=lambda x: alg_score[x], reverse=True))
    sorted_requests = [requests_list[i] for i in sorted_keys]
    if len(sorted_requests) < 4:
        return sorted_requests
    else:
        return sorted_requests[:3]  # return request with the highest score

