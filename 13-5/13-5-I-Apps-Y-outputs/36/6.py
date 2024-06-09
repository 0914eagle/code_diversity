
def solve(x, y):
    for cranes in range(x+1):
        turtles = x-cranes
        if 2*cranes + 4*turtles == y:
            return "Yes"
    return "No"

