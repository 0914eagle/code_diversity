
def input_data():
    n, k = map(int, input().split())
    return n, k

def find_number_of_ways(n, k):
    # Initialize a list to store the number of ways to place the plaques
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # If i is less than or equal to k, the penguin can go back to house number 1
        if i <= k:
            ways[i] = (ways[i - 1] + ways[i - 2]) % 1000000007
        # Otherwise, the penguin cannot go back to house number 1
        else:
            ways[i] = ways[i - 1]
    
    return ways[n]

def main():
    n, k = input_data()
    print(find_number_of_ways(n, k) % 1000000007)

if __name__ == '__main__':
    main()

