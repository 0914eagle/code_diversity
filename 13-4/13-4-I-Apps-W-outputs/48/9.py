
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
            if a[i] == a[i + 1]:  # Same shape
                points -= 2
            elif a[i] == 1 and a[i + 1] == 2:  # Circle and triangle
                points -= 1
            elif a[i] == 2 and a[i + 1] == 1:  # Triangle and circle
                points -= 1
            elif a[i] == 1 and a[i + 1] == 3:  # Circle and square
                points -= 2
            elif a[i] == 3 and a[i + 1] == 1:  # Square and circle
                points -= 2
    
    if points < 0:
        return "Infinite", None
    else:
        return "Finite", points

