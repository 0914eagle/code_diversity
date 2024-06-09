
def is_triangle(sticks):
    
    sticks.sort()
    for i in range(len(sticks) - 2):
        a = sticks[i]
        for j in range(i + 1, len(sticks) - 1):
            b = sticks[j]
            c = sticks[j + 1]
            if a + b > c and b + c > a and a + c > b:
                return "possible"
    return "impossible"

