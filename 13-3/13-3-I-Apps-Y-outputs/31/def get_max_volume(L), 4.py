
def get_max_volume(L):
    
    # Initialize the variables to find the maximum volume
    a = b = c = 0
    max_volume = 0

    # Loop through all possible combinations of a, b, and c
    for i in range(1, L + 1):
        for j in range(1, L + 1 - i):
            k = L - i - j
            if i * j * k > max_volume:
                a = i
                b = j
                c = k
                max_volume = i * j * k

    return max_volume

