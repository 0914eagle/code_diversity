
def solve(p, n):
    # Initialize a dictionary to store the number of days each kid has owned their book
    days_owned = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the permutation p
    for i in range(1, n + 1):
        # Find the current owner of the book
        current_owner = p[i - 1]
        # Increment the number of days the owner has owned the book
        days_owned[current_owner] += 1
        # Set the next owner in the permutation
        p[i - 1] = p[current_owner - 1]
    
    # Return the number of days each kid has owned their book
    return [days_owned[i] for i in range(1, n + 1)]

def main():
    # Read the number of queries
    q = int(input())
    
    # Iterate through each query
    for _ in range(q):
        # Read the number of kids and the permutation
        n = int(input())
        p = list(map(int, input().split()))
        
        # Solve the query and print the answer
        print(*solve(p, n))

if __name__ == '__main__':
    main()

