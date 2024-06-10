
def count_ways(n, k):
    # Base case: if n is 0, there is only one way to paint the balls
    if n == 0:
        return 1
    
    # Recursive case: count the number of ways to paint the balls
    # by counting the number of ways to paint the first ball and
    # the number of ways to paint the remaining balls
    return k * count_ways(n - 1, k)

def main():
    # Read the input data from stdin
    n, k = map(int, input().split())
    
    # Print the number of possible ways to paint the balls
    print(count_ways(n, k))

if __name__ == '__main__':
    main()

