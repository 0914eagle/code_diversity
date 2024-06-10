
def get_number_of_ways(n, k):
    # Initialize a list to store the number of ways for each house
    number_of_ways = [0] * (n + 1)
    number_of_ways[0] = 1
    
    # Loop through each house and calculate the number of ways to reach it
    for i in range(1, n + 1):
        number_of_ways[i] = (number_of_ways[i - 1] + number_of_ways[i - k - 1]) % 1000000007
    
    return number_of_ways[n]

def main():
    n, k = map(int, input().split())
    print(get_number_of_ways(n, k))

if __name__ == '__main__':
    main()

