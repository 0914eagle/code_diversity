
def solve(s, queries):
    # Initialize a counter for the number of queries
    count = 0
    
    # Iterate through the queries
    for l, r in queries:
        # Count the number of indices i such that s[i] = s[i] + 1
        count += sum(s[l:r])
        
    # Return the count
    return count

def main():
    # Read the input string and the number of queries
    s = input()
    m = int(input())
    
    # Read the queries
    queries = []
    for i in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))
    
    # Solve the problem
    count = solve(s, queries)
    
    # Print the result
    print(count)

if __name__ == '__main__':
    main()

