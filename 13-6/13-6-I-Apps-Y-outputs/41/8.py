
def get_days_till_next_sunday(day_of_week):
    days_till_sunday = {
        "MON": 6,
        "TUE": 5,
        "WED": 4,
        "THU": 3,
        "FRI": 2,
        "SAT": 1,
        "SUN": 0,
    }
    return days_till_sunday[day_of_week]

