
def find_longest_substring(s, t):
    # Initialize variables
    longest_substring = 0
    current_substring = 0
    s_idx = 0
    t_idx = 0

    # Loop through both strings
    while s_idx < len(s) and t_idx < len(t):
        if s[s_idx] == t[t_idx]:
            # If characters match, increment current substring
            current_substring += 1
            t_idx += 1
        else:
            # If characters don't match, reset current substring
            current_substring = 0
        longest_substring = max(longest_substring, current_substring)
        s_idx += 1

    return longest_substring

def main():
    s = input("Enter string s: ")
    t = input("Enter string t: ")
    print(find_longest_substring(s, t))

if __name__ == '__main__':
    main()

