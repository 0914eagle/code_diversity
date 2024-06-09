
def is_power_of_three_and_five(n):
    for i in range(1, n+1):
        if 3**i + 5**i == n:
            return True
    return False

