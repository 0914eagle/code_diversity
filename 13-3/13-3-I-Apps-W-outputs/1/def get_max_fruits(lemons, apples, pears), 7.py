
def get_max_fruits(lemons, apples, pears):
    if lemons == 0 and apples == 0 and pears == 0:
        return 0

    lemons_needed = apples * 2 + pears * 4
    apples_needed = lemons * 2 + pears * 4
    pears_needed = lemons * 4 + apples * 2

    lemons_available = min(lemons, lemons_needed)
    apples_available = min(apples, apples_needed)
    pears_available = min(pears, pears_needed)

    return lemons_available + apples_available + pears_available

