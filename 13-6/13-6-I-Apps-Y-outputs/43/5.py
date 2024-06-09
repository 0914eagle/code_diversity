
def count_ways(n, k):
    # Base case: if there are no balls, there is only one way to paint them
    if n == 0:
        return 1
    
    # Recursive case: count the number of ways to paint the balls
    return k * count_ways(n - 1, k)

def main():
    # Read the input from stdin
    n, k = map(int, input().split())
    
    # Call the count_ways function and print the result
    print(count_ways(n, k))

if __name__ == '__main__':
    main()

