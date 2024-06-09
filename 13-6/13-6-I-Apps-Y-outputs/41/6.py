
def next_sunday(day):
    days = {"SUN": 0, "MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6}
    return (7 - days[day]) % 7

