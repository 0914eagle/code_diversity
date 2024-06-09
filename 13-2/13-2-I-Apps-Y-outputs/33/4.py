
def get_free_food_days(events):
    days = set()
    for s, t in events:
        for i in range(s, t+1):
            days.add(i)
    return len(days)

