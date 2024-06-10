
def find_day_of_first_return(p, n):
    # Initialize a dictionary to store the day of first return for each kid
    days = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the permutation p
    for i in range(1, n + 1):
        # Find the current owner of the book
        current_owner = p[i - 1]
        
        # If the current owner is not the kid itself, update the day of first return
        if current_owner != i:
            days[current_owner] = max(days[current_owner], days[i] + 1)
    
    # Return the day of first return for each kid
    return [days[i] for i in range(1, n + 1)]

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(*find_day_of_first_return(p, n))

if __name__ == '__main__':
    main()

