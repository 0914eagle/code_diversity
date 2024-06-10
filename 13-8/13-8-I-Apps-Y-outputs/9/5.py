
def get_maximum_candies(n, k):
    # Initialize variables
    a = 0
    b = 0
    count = 0
    
    # Loop through all possible values of a
    for a in range(n):
        # Calculate b based on the conditions
        b = n - a
        if b - a <= 1 and count <= k // 2:
            count += 1
        else:
            break
    
    # Return the maximum number of candies that can be given to kids
    return a + b

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(get_maximum_candies(n, k))

if __name__ == '__main__':
    main()

