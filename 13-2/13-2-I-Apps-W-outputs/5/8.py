
def reconstruct_string(n, t_k_x):
    # Initialize an empty string
    s = ""
    
    # Sort the input data by the length of the strings and their positions
    sorted_data = sorted(t_k_x, key=lambda x: (len(x[0]), x[2]))
    
    # Iterate through the sorted data
    for t, k, x in sorted_data:
        # If the string is not already in the output string
        if t not in s:
            # Add the string to the output string
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

