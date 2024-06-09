
def solve(x, queue):
    num_women = 0
    num_men = 0
    max_people = 0
    for person in queue:
        if person == "W":
            num_women += 1
        else:
            num_men += 1
        if abs(num_women - num_men) > x:
            return max_people
        max_people += 1
    return max_people

