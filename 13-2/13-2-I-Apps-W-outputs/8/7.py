
def check_production_stops(a, m):
    while a >= m:
        a = a % m
    if a == 0:
        return "Yes"
    else:
        return "No"

