def add_time(start, duration, dd=''):
    time = start.split()
    hour_start = time[0].split(":")[0]
    minute_start = time[0].split(":")[1]
    hour_dur = duration.split(":")[0]
    minute_dur = duration.split(":")[1]
    ampm = ["AM", "PM"]
    night = start.split()[1]
    day = 0
    if int(hour_start) == 12:
        hour_start = 0

    if night == ampm[1]:
        hour_start = int(hour_start) + 12

    tot_min = int(minute_start) + int(minute_dur)
    tot_hour = int(hour_dur) + int(hour_start)

    if tot_min >= 60:
        tot_hour += (tot_min//60)
        tot_min -= 60
    if tot_hour >= 24:
        day += tot_hour//24
        tot_hour -= 24*day

    if tot_hour == 0:
        tot_hour = 12
    if tot_hour == 12 and (int(minute_start) + int(minute_dur)) >= 60 and night == "AM":
        night = "PM"
    elif tot_hour == 12 and (int(minute_start) + int(minute_dur)) >= 60 and night == "PM":
        night = "AM"
    elif tot_hour - 12 > 0:
        tot_hour -= 12
        night = "PM"
    else:
        night = "AM"

    if dd == '':
        if day == 1:
            result = "{:d}:{:02d} {:} (next day)".format(tot_hour, tot_min, night)
        elif day > 1:
            result = "{:d}:{:02d} {:} ({:d} days later)".format(tot_hour, tot_min, night, day)
        else:
            result = "{:d}:{:02d} {:}".format(tot_hour, tot_min, night)

    else:
        list_hari = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        hari = dd.capitalize()

        day_num = 0
        for i in range(len(list_hari)):
            if hari == list_hari[i]:
                day_num = i
        day_num += day
        day_num %= 7
        if day == 1:
            result = "{:d}:{:02d} {:}, {:} (next day)".format(tot_hour, tot_min, night, list_hari[day_num])
        elif day > 1:
            result = "{:d}:{:02d} {:}, {:} ({:d} days later)".format(tot_hour, tot_min, night, list_hari[day_num], day)
        else:
            result = "{:d}:{:02d} {:}, {:}".format(tot_hour, tot_min, night, list_hari[day_num])

    return result


# For testing
# print(add_time("3:00 PM", "3:10"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("6:30 PM", "205:12"))
