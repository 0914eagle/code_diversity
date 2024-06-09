
def is_takahashi(day, month):
    return day == month

def count_takahashi_days(a, b):
    count = 0
    for day in range(1, b+1):
        if is_takahashi(day, a):
            count += 1
    return count

