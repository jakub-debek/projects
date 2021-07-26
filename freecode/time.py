def add_time(start, duration, day = False):

    split_start = start.split(" ")
    meridiem = split_start[-1]
    split_time_start = split_start[0].split(":")
    hour_start = int(split_time_start[0])
    minute_start = int(split_time_start[1])

    duration_split = duration.split(":")
    hour_duration = int(duration_split[0])
    minute_duration = int(duration_split[1])

    hour = hour_start + hour_duration
    day_count = 0
    next_day = ""

    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
    day_index = 0
    week = ""

    if minute_duration + minute_start > 59:
        hour += 1
        minute = minute_duration + minute_start - 60
    else:
        minute = minute_duration + minute_start

    if minute < 10:
        minute = f"0{minute}"

    while True:
        if hour > 12:
            hour += -12
            if meridiem == "PM":
                meridiem = "AM"
                day_count += 1
            else:
                meridiem = "PM"
        elif hour == 12:
            if meridiem == "PM":
                meridiem = "AM"
                day_count += 1
                break
            else:
                meridiem = "PM"
                break
        else:
            break

    if day_count > 0:
        if day_count == 1:
            next_day = "(next day)"
        else:
            next_day = f" ({day_count} days later)"


    if day:
        day = day.lower()
        day_index = (day_of_week_index[day] + day_count) % 7
        week = f", {day_of_week[day_index]}"

    end = f"{hour}:{minute} {meridiem}{week}{next_day}"

    return end


print(add_time("8:16 PM", "466:02", "tuesday"))
