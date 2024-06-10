
def get_number_of_ways(n, k, lamps):
    # Initialize a dictionary to store the number of ways for each combination of lamps
    number_of_ways = {}
    
    # Iterate over all possible combinations of lamps
    for combination in combinations(lamps, k):
        # Initialize a flag to indicate if the combination is valid
        valid_combination = True
        
        # Iterate over all lamps in the combination
        for lamp in combination:
            # If any lamp is not turned on at the same time, the combination is not valid
            if lamp not in lamps[lamp]:
                valid_combination = False
                break
        
        # If the combination is valid, increment the number of ways
        if valid_combination:
            number_of_ways[combination] = number_of_ways.get(combination, 0) + 1
    
    # Return the number of ways modulo 998244353
    return sum(number_of_ways.values()) % 998244353

def main():
    n, k = map(int, input().split())
    lamps = [set(map(int, input().split())) for _ in range(n)]
    print(get_number_of_ways(n, k, lamps))

if __name__ == '__main__':
    main()

