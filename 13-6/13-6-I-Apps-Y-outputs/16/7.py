
def solve(p, n):
    # Initialize a dictionary to store the number of days each kid has owned their book
    days_owned = {i: 0 for i in range(1, n + 1)}
    
    # Loop through each day
    for day in range(1, n + 1):
        # Loop through each kid and update the number of days they have owned their book
        for i in range(1, n + 1):
            days_owned[i] += 1
            if p[i - 1] == i:
                days_owned[i] = 0
    
    # Return the number of days each kid has owned their book
    return [days_owned[i] for i in range(1, n + 1)]

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(*solve(p, n))

if __name__ == '__main__':
    main()

