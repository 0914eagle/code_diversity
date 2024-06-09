
def next_sunday(day):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return (days.index(day) - days.index("SUN") + 1) % 7

