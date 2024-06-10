
def read_input():
    n, k = map(int, input().split())
    return n, k

def find_number_of_ways(n, k):
    # Initialize a list to store the number of ways to write the numbers on the houses' plaques
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Iterate through each house and calculate the number of ways to write the number on the plaque
    for i in range(1, n + 1):
        ways[i] = sum(ways[j] for j in range(i, min(i + k, n + 1)))
    
    # Return the number of ways modulo 1000000007
    return ways[n] % 1000000007

def main():
    n, k = read_input()
    print(find_number_of_ways(n, k))

if __name__ == '__main__':
    main()

