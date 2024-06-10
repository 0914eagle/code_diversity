
def get_max_substring_length(s, t):
    # Initialize variables
    max_len = 0
    s_len = len(s)
    t_len = len(t)
    # Loop through all possible starting indices of t in s
    for i in range(s_len - t_len + 1):
        # Check if t is a subsequence of s starting from index i
        if s[i:i+t_len] == t:
            # If it is, update the maximum length
            max_len = max(max_len, t_len)
    # Return the maximum length
    return max_len

def main():
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")
    print(get_max_substring_length(s, t))

if __name__ == '__main__':
    main()

