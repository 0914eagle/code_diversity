
def get_max_volume(L):
    
    # Initialize the variables to find the maximum volume
    a = 0
    b = 0
    c = 0
    volume = 0

    # Loop through all possible combinations of a, b, and c
    for i in range(1, L + 1):
        for j in range(1, L + 1 - i):
            k = L - i - j
            if i * j * k > volume:
                a = i
                b = j
                c = k
                volume = i * j * k

    return volume

