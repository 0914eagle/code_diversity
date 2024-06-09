
def number_of_ways_to_fill_tiles(n):
    # Initialize a list to store the number of ways to fill each row
    ways = [0] * (n + 1)
    ways[0] = 1
    
    for i in range(1, n + 1):
        # The number of ways to fill the ith row is the sum of the number of ways to fill the (i-1)th row and the (i-2)th row
        ways[i] = ways[i - 1] + ways[i - 2]
    
    return ways[n]

def main():
    n = int(input())
    print(number_of_ways_to_fill_tiles(n))

if __name__ == '__main__':
    main()

