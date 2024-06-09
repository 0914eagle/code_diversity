
def get_points(a, b, c, d):
    misha_points = max(a // 10, a - (a // 250) * c)
    vasya_points = max(b // 10, b - (b // 250) * d)
    if misha_points > vasya_points:
        return "Misha"
    elif misha_points < vasya_points:
        return "Vasya"
    else:
        return "Tie"

