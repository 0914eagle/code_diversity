
def get_lamps(n, k, lamps):
    # Initialize a set to store the indices of the lamps that are on
    on_lamps = set()
    
    # Iterate over the lamps and check if they are on at the same time
    for i in range(n):
        for j in range(i+1, n):
            # If the lamps are on at the same time, add them to the set
            if lamps[i][0] <= lamps[j][1] and lamps[i][1] >= lamps[j][0]:
                on_lamps.add(i)
                on_lamps.add(j)
    
    # Return the number of ways to choose k lamps from the on_lamps set
    return len(list(combinations(on_lamps, k))) % 998244353

def main():
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        l, r = map(int, input().split())
        lamps.append([l, r])
    print(get_lamps(n, k, lamps))

if __name__ == '__main__':
    main()

