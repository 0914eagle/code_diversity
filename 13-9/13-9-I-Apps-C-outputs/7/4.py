
def get_number_of_ways(n, k):
    # Initialize a list to store the number of ways for each house
    num_ways = [0] * (n + 1)
    num_ways[1] = 1
    
    for i in range(2, n + 1):
        # For each house, calculate the number of ways to get to it from house 1
        num_ways[i] = (num_ways[i - 1] + num_ways[i - 2]) % 1000000007
    
    return num_ways[n]

def main():
    n, k = map(int, input().split())
    print(get_number_of_ways(n, k))

if __name__ == '__main__':
    main()

