
def read_notes(a, b):
    # Initialize variables
    n = 0
    p = []
    m = 0
    q = []
    
    # Loop through all possible note numbers
    for i in range(1, a+b+1):
        # Check if the current note can be read in the first day
        if i <= a:
            n += 1
            p.append(i)
        # Check if the current note can be read in the second day
        if a < i <= a+b:
            m += 1
            q.append(i)
    
    # Return the results
    return n, p, m, q

def main():
    # Read input
    a, b = map(int, input().split())
    
    # Call the read_notes function
    n, p, m, q = read_notes(a, b)
    
    # Print the results
    print(n)
    print(*p)
    print(m)
    print(*q)

if __name__ == '__main__':
    main()

