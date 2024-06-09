
def get_hours_until_new_year(hour):
    if hour < 0 or hour > 23:
        raise ValueError("Invalid hour")
    return 24 - hour

