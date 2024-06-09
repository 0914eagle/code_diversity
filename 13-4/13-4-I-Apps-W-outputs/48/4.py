
def solve(n, a):
    # Calculate the number of distinct points where figures touch
    points = 0
    for i in range(n):
        if a[i] == 1:  # Circle
            points += 1
        elif a[i] == 2:  # Isosceles triangle
            points += 2
        else:  # Square
            points += 4
    
    # Check if the number of points is infinite
    if n == 1:
        return "Finite", points
    else:
        for i in range(n - 1):
            if a[i] == a[i + 1]:  # Same type of figures touching
                return "Infinite", 0
        
        return "Finite", points

