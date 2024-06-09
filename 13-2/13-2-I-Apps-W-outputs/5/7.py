
def reconstruct_string(n, t_k_x):
    # Initialize an empty string
    s = ""
    
    # Sort the input data by the length of the strings and their positions
    t_k_x.sort(key=lambda x: (len(x[0]), x[1], x[2]))
    
    # Loop through the input data
    for t, k, x in t_k_x:
        # If the string is not empty, append it to the output string
        if t:
            s += t
    
    # Return the lexicographically minimal string
    return s

def main():
    # Read the input data
    n = int(input())
    t_k_x = []
    for _ in range(n):
        t, k, *x = input().split()
        t_k_x.append((t, int(k), [int(i) for i in x]))
    
    # Call the reconstruct_string function
    s = reconstruct_string(n, t_k_x)
    
    # Print the output
    print(s)

if __name__ == '__main__':
    main()

