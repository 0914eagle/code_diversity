
def check_production_stop(a, m):
    while a >= 0:
        if a % m == 0:
            return "Yes"
        a += 1
    return "No"

