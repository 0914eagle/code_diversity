
def get_days_with_free_food(events):
    days = set()
    for s, t in events:
        for i in range(s, t+1):
            days.add(i)
    return len(days)

