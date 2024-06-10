
def read_input():
    n, k = map(int, input().split())
    return n, k

def solve(n, k):
    # Initialize the number of ways as 1
    ways = 1
    
    # Iterate from 1 to k
    for i in range(1, k + 1):
        # Update the number of ways by the number of ways to write the plaques
        # such that the penguin can walk back to house number 1 after i walks
        ways = (ways * (i ** (n - i))) % 1000000007
    
    # Return the number of ways modulo 1000000007
    return ways

def main():
    n, k = read_input()
    print(solve(n, k))

if __name__ == '__main__':
    main()

