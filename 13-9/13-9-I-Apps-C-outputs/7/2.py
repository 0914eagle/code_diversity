
def read_input():
    n, k = map(int, input().split())
    return n, k

def walk(n, k):
    # Initialize the number of ways as 1
    ways = 1
    
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # If the current house is less than or equal to k, we can walk to house number 1
        if i <= k:
            ways = (ways * (n - i + 1)) % 1000000007
        # If the current house is greater than k, we cannot walk to house number 1
        else:
            ways = (ways * i) % 1000000007
    
    return ways

def main():
    n, k = read_input()
    print(walk(n, k))

if __name__ == '__main__':
    main()

