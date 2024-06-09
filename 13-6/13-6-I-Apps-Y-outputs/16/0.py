
def find_first_return_day(n, p):
    # Initialize a list to store the first return day for each kid
    first_return_day = [0] * n
    
    # Iterate through each day
    for day in range(1, n + 1):
        # Iterate through each kid
        for kid in range(n):
            # If the kid's book is returned to him, set the first return day for that kid
            if p[kid] == kid:
                first_return_day[kid] = day
                break
    
    return first_return_day

def main():
    # Read the number of queries
    q = int(input())
    
    # Iterate through each query
    for _ in range(q):
        # Read the number of kids and the permutation
        n = int(input())
        p = list(map(int, input().split()))
        
        # Find the first return day for each kid
        first_return_day = find_first_return_day(n, p)
        
        # Print the first return day for each kid
        print(*first_return_day)

if __name__ == '__main__':
    main()

