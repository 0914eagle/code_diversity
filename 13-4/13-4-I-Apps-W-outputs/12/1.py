
def get_min_missed_meals(breakfasts, dinners, suppers):
    total_meals = breakfasts + dinners + suppers
    if total_meals == 0:
        return 0
    elif total_meals == 1:
        return 1
    elif total_meals == 2:
        return 2
    else:
        return total_meals - 1

