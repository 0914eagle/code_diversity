
def solve(n):
    car_makes = ["A", "B", "M", "Z"]
    ways = 0
    for i in range(len(car_makes)):
        for j in range(i+1, len(car_makes)):
            for k in range(j+1, len(car_makes)):
                for l in range(k+1, len(car_makes)):
                    if n == 1:
                        ways += 1
                    else:
                        ways += solve(n-1)
    return ways

