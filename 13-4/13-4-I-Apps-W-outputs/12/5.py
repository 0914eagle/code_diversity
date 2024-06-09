
def get_min_missed_meals(breakfasts, dinners, suppers):
    return max(0, breakfasts + dinners + suppers - 2)

