
def count_takahashi_days(a, b):
    takahashi_days = 0
    for day in range(1, b+1):
        if day == a:
            takahashi_days += 1
    return takahashi_days

