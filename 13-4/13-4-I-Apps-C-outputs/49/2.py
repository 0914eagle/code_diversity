
def get_max_eligible_pupils(pupils):
    max_eligible = 0
    for i in range(len(pupils)):
        for j in range(i+1, len(pupils)):
            if (abs(pupils[i][0] - pupils[j][0]) > 40 or
                pupils[i][1] != pupils[j][1] or
                pupils[i][2] != pupils[j][2] or
                pupils[i][3] == pupils[j][3]):
                max_eligible += 1
    return max_eligible

