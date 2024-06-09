
def next_sunday(day):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    today_idx = days.index(day)
    return (7 - today_idx) % 7

