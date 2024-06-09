
def get_days_to_next_sunday(day):
    days = {
        "SUN": 0,
        "MON": 6,
        "TUE": 5,
        "WED": 4,
        "THU": 3,
        "FRI": 2,
        "SAT": 1
    }
    return days[day]

