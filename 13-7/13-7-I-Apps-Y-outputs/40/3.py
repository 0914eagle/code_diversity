
def is_consistent(capacity, stations):
    total = 0
    for left, arrived, stayed in stations:
        total += arrived - left
        if total < 0 or stayed > 0:
            return "impossible"
    return "possible" if total == 0 else "impossible"

