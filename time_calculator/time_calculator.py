def add_time(start, duration, argument3 = False):
    result = dict()
    reference_time = "AM"
    condition = False 

    arg1_24 = start.split()
    arg2_24 = duration.split(":")

    current_time = arg1_24[0].split(":")

    if arg1_24[1] == "PM":
        current_time[0] = int(current_time[0]) + 12
   
    hours = int(current_time[0]) + int(arg2_24[0])
    minute = int(current_time[1]) + int(arg2_24[1])

    tmpH = hours
    tmpM = minute
    tmpD = 0

    if minute > 60 :
        tmpH = int(minute / 60)
        tmpM = minute - tmpH*60
        tmpD = int(tmpH/24)
        condition = True
#new time
    if condition: 
        hours = hours + tmpH 
        tmpH =  hours

    if hours > 24 :    
        tmpD = int(hours/24) 
        tmpH = hours - tmpD*24
    result = {"day": tmpD, "hour" : tmpH, "minut" : tmpM}
#definng PM or AM
    if result['hour'] >= 0 and result['hour'] < 12:
        reference_time = "AM"
    else :
        reference_time = "PM"
# redefind hours
    if result["hour"] == 0:
        result["hour"] = 12
    if result['hour'] > 12 :
        result["hour"] = result["hour"] - 12
# preparing returning value for printing 
    if not argument3 == False :
        return f"{result['hour']}" + ":" +f"{result['minut']:02d}" + " " + reference_time + display_day(argument3, result)
    else :
        return f"{result['hour']}"+ ":" +f"{result['minut']:02d}" + " " + reference_time + display_day(argument3, result)

# calculate the day in the week and number of days
def display_day(argument3, result):
    if not argument3 == False :
        argument3.lower()
        argument3 = argument3.capitalize()
        days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        if result["day"] == 0:
            return f", {argument3}"
        elif result["day"] == 1:
            tmp_pos = days.index(argument3)
            day_pos = (result['day'] + tmp_pos)%7
            return f", {days[day_pos]}" + " (next day)"
        else :
            tmp_pos = days.index(argument3)
            day_pos = (result['day'] + tmp_pos)%7
            return f", {days[day_pos]}" + f" ({result['day']}" + " days later)"
    else :
        if result["day"] == 0:
            return ""
        elif result["day"] == 1:
            return " (next day)"
        else :
            return f" ({result['day']}" + " days later)"
