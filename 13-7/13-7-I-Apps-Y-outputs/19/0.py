
def get_hours_until_new_year(hour):
    if hour < 24:
        return 24 - hour
    else:
        return 24 - (hour - 24)

