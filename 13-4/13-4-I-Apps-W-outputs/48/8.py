
def solve(n, a):
    # Calculate the number of distinct points where figures touch
    points = 0
    for i in range(n):
        if a[i] == 1:  # Circle
            points += 2
        elif a[i] == 2:  # Isosceles triangle
            points += 3
        else:  # Square
            points += 4
    return "Finite" if points < 100 else "Infinite"

