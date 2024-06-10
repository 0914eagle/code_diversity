
def get_amidakuji_count(h, w, k):
    # Initialize a list to store the number of valid amidakuji
    amidakuji_count = 0
    
    # Loop through each possible combination of horizontal lines
    for i in range(1, w+1):
        for j in range(1, h+1):
            # Check if the current combination of horizontal lines satisfies the conditions
            if is_valid_amidakuji(i, j, k, h, w):
                amidakuji_count += 1
    
    # Return the number of valid amidakuji
    return amidakuji_count

def is_valid_amidakuji(i, j, k, h, w):
    # Check if the current combination of horizontal lines satisfies the conditions
    if i > w or j > h:
        return False
    if i == w and j != k:
        return False
    if i != w and j == h:
        return False
    if i != w and j != h and (i+j) % 2 == 0:
        return False
    return True

if __name__ == '__main__':
    h, w, k = map(int, input().split())
    print(get_amidakuji_count(h, w, k))

