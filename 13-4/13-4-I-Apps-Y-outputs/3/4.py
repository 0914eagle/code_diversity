
def get_days_till_next_sunday(day_of_week):
    days_till_sunday = {
        "SUN": 0,
        "MON": 6,
        "TUE": 5,
        "WED": 4,
        "THU": 3,
        "FRI": 2,
        "SAT": 1,
    }
    return days_till_sunday[day_of_week]

