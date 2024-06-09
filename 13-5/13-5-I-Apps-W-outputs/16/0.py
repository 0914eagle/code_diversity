
def solve(cows_per_day, number_of_farms, days_visited, days_visited_list):
    farms_inspected = 0
    for day in range(1, days_visited+1):
        for i in range(number_of_farms):
            if cows_per_day[i] > cows_per_day[i] // 2:
                farms_inspected += 1
        cows_per_day = [cows_per_day[i] // 2 for i in range(number_of_farms)]
    return farms_inspected

