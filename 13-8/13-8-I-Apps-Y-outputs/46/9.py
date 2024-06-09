
def cost_of_ferris_wheel(age, cost):
    if age >= 13:
        return cost
    elif 6 <= age <= 12:
        return cost // 2
    else:
        return 0

