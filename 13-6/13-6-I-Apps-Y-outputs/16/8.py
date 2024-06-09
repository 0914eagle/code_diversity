
def solve(p, n):
    # Initialize a dictionary to store the number of days for each kid
    days = {i: 0 for i in range(1, n + 1)}
    
    # Loop through each day
    for day in range(1, n):
        # Loop through each kid
        for i in range(1, n + 1):
            # If the current kid is the owner of the book, increase the number of days by 1
            if i == p[i - 1]:
                days[i] += 1
    
    # Return the number of days for each kid
    return [days[i] for i in range(1, n + 1)]

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(*solve(p, n))

if __name__ == '__main__':
    main()

