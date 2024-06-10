
def read_input():
    n, k = map(int, input().split())
    return n, k

def get_number_of_ways(n, k):
    # Initialize a list to store the number of ways to write the numbers on the plaques
    ways = [0] * (n + 1)
    ways[0] = 1
    
    for i in range(1, n + 1):
        if i <= k:
            ways[i] = (ways[i - 1] + ways[i - 1] * (n - i + 1)) % 1000000007
        else:
            ways[i] = (ways[i - 1] - ways[i - k - 1]) % 1000000007
    
    return ways[n]

def main():
    n, k = read_input()
    print(get_number_of_ways(n, k))

if __name__ == '__main__':
    main()

