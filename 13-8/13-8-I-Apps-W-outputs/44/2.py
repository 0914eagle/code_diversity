
def find_badge_holder(n, p):
    badge_holder = 1
    for i in range(n):
        badge_holder = p[badge_holder - 1]
    return badge_holder

