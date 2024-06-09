
def worst_case_scenario(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    return 2 * (n - 1) + 1

