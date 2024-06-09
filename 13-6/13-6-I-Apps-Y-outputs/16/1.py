
def solve(p, n):
    # Initialize a dictionary to store the number of days each kid has owned their book
    days_owned = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the permutation p
    for i in range(1, n + 1):
        # If the current kid is the owner of the book, increment the number of days they have owned it
        if p[i - 1] == i:
            days_owned[i] += 1
        # Otherwise, find the next kid in the permutation who will own the book and increment their number of days owned
        else:
            days_owned[p[i - 1]] += 1
    
    # Return the number of days each kid has owned their book
    return [days_owned[i] for i in range(1, n + 1)]

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        result = solve(p, n)
        print(" ".join(map(str, result)))

if __name__ == '__main__':
    main()

