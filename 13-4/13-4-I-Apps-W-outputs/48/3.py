
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
    
    # Check if the number of points is infinite
    if n > 1 and a[1] == 3 and a[2] == 1:  # Triangle and circle touch each other for the whole segment
        return "Infinite"
    
    return "Finite", points

