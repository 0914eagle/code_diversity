
def reconstruct_string(n, t_k_x):
    # Initialize an empty string
    s = ""
    
    # Sort the tuples in increasing order of the first element (string t)
    t_k_x.sort(key=lambda x: x[0])
    
    # Iterate through the tuples
    for t, k, x in t_k_x:
        # If the string t is not empty, add it to the string s
        if t:
            s += t
    
    # Return the lexicographically minimal string s
    return s

def main():
    # Read the number of strings n and their information
    n = int(input())
    t_k_x = []
    for _ in range(n):
        t, k, *x = input().split()
        t_k_x.append((t, int(k), [int(i) for i in x]))
    
    # Reconstruct the string s
    s = reconstruct_string(n, t_k_x)
    
    # Print the lexicographically minimal string s
    print(s)

if __name__ == '__main__':
    main()

