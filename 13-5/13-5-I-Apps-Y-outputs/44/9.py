
def is_takahashi(month, day):
    return month == day

def count_takahashi_days(a, b):
    count = 0
    for day in range(1, b+1):
        if is_takahashi(a, day):
            count += 1
    return count

