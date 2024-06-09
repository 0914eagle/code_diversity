
def solve(p, n):
    # Initialize a dictionary to store the number of days each kid has owned their book
    days_owned = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the permutation p
    for i in range(n):
        # Find the current owner of the book
        current_owner = p[i]
        
        # If the current owner is the same as the current kid, it means the book has returned to its owner
        if current_owner == i + 1:
            # Increment the number of days the book has been owned by the current kid
            days_owned[i + 1] += 1
        else:
            # If the current owner is not the current kid, it means the book has been passed on to the next kid
            # Increment the number of days the book has been owned by the next kid
            days_owned[current_owner] += 1
    
    # Return the number of days each kid has owned their book
    return [days_owned[i] for i in range(1, n + 1)]

def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(*solve(p, n))

if __name__ == '__main__':
    main()

