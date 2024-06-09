
def check_package(n, a, b, c, d):
    for i in range(n):
        x = a + b
        if x < c or x > d:
            return "No"
    return "Yes"

