
def check_production_stops(a, m):
    while a > 0:
        a += a % m
        if a % m == 0:
            return "Yes"
    return "No"

