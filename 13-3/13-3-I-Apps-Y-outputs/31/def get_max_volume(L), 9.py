
def get_max_volume(L):
    # Initialize the variables to brute force
    a = 1
    b = 1
    c = 1
    
    # Loop through all possible combinations of a and b
    while a <= L/2:
        b = L/a
        while b >= 1:
            c = L/a/b
            if a + b + c == L:
                return a*b*c
            b -= 1
        a += 1
    return 0

