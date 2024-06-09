
def reconstruct_string(n, t_k_x):
    # Initialize an empty string
    s = ""
    
    # Sort the tuples in increasing order of the first element (string t)
    t_k_x.sort(key=lambda x: x[0])
    
    # Iterate through the tuples
    for t, k, x in t_k_x:
        # Append the string t to s k times
        s += t * k
    
    # Return the lexicographically minimal string
    return s

def main():
    # Read the number of strings
    n = int(input())
    
    # Read the information about the strings
    t_k_x = []
    for _ in range(n):
        t, k, *x = input().split()
        t_k_x.append((t, int(k), [int(i) for i in x]))
    
    # Reconstruct the string
    s = reconstruct_string(n, t_k_x)
    
    # Print the result
    print(s)

if __name__ == '__main__':
    main()

