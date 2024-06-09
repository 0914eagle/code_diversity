
def count_problem_sets(n, l, r, x, c):
    # Sort the difficulties in non-decreasing order
    c.sort()
    
    # Initialize the number of problem sets to 0
    count = 0
    
    # Loop through all possible starting points for the problem set
    for i in range(n):
        # Check if the total difficulty of the problem set is within the given range
        if c[i] + c[i+1] >= l and c[i] + c[i+1] <= r:
            # Check if the difference in difficulty between the hardest and easiest problems is at least x
            if abs(c[i] - c[i+1]) >= x:
                # Increment the number of problem sets
                count += 1
    
    return count

def main():
    n, l, r, x = map(int, input().split())
    c = list(map(int, input().split()))
    print(count_problem_sets(n, l, r, x, c))

if __name__ == '__main__':
    main()

