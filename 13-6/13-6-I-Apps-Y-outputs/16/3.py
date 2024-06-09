
def get_first_return_days(n, p):
    # Initialize a list to store the first return days for each kid
    first_return_days = [0] * n
    
    # Iterate through the permutation p
    for i in range(n):
        # If the kid's book is not already returned to him, update the first return day
        if first_return_days[i] == 0:
            first_return_days[i] = i + 1
    
    # Return the list of first return days
    return first_return_days

def get_first_return_day(n, p, kid):
    # Get the first return days for all kids
    first_return_days = get_first_return_days(n, p)
    
    # Return the first return day for the given kid
    return first_return_days[kid - 1]

if __name__ == '__main__':
    q = int(input())
    
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        kid = int(input())
        
        print(get_first_return_day(n, p, kid))

