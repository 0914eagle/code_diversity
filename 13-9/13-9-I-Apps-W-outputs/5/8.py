
def get_lamps(n, k, lamps):
    # Initialize a dictionary to store the number of lamps that are on at each time
    lamps_on = {}
    for i in range(1, 10**9 + 1):
        lamps_on[i] = 0
    for l, r in lamps:
        for i in range(l, r + 1):
            lamps_on[i] += 1
    
    # Initialize a counter to store the number of combinations
    count = 0
    
    # Iterate through the dictionary and check if the number of lamps that are on at each time is greater than or equal to k
    for i in range(1, 10**9 + 1):
        if lamps_on[i] >= k:
            count += 1
    
    # Return the number of combinations modulo 998244353
    return count % 998244353

def main():
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        l, r = map(int, input().split())
        lamps.append((l, r))
    print(get_lamps(n, k, lamps))

if __name__ == '__main__':
    main()

