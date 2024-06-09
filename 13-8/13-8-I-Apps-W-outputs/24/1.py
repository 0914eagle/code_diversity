
def is_solvable(a, b, c):
    # Calculate the slope of the line that passes through points a and b
    m1 = (b[1] - a[1]) / (b[0] - a[0])
    # Calculate the slope of the line that passes through points a and c
    m2 = (c[1] - a[1]) / (c[0] - a[0])
    # Check if the slopes are equal
    if m1 == m2:
        return "Yes"
    else:
        return "No"

