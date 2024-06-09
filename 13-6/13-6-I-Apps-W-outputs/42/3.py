
def get_number_of_ways(n, k, lamps):
    # Initialize a list to store the number of ways to turn on k lamps
    num_ways = [0] * (k + 1)
    num_ways[0] = 1
    
    for i in range(n):
        for j in range(k, 0, -1):
            if lamps[i][0] <= j:
                num_ways[j] += num_ways[j - lamps[i][0]]
    
    return num_ways[k] % 998244353

def main():
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        lamps.append(list(map(int, input().split())))
    
    print(get_number_of_ways(n, k, lamps))

if __name__ == '__main__':
    main()

