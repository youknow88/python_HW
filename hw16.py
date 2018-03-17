def have_trains_crashed(v1, v2):
    distance1 = 4
    time1 = v1 / distance1
    distance2 = 6
    time2 = v2 / distance2
    if time1 <= time2:
        return True
    if time1 > time2:
        return False

print(have_trains_crashed(130, 80))