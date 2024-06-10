
def get_good_substrings(s):
    # Initialize variables
    k = 0
    substrings = []
    
    # Iterate through the string
    for i in range(len(s)):
        # If the current character is a 1, add it to the current substring
        if s[i] == "1":
            substrings.append(s[i])
        # If the current character is a 0 and the substring is not empty, add it to the list of substrings
        elif s[i] == "0" and substrings:
            k += 1
            substrings.append(s[i])
    
    # If the last substring is not empty, add it to the list of substrings
    if substrings:
        k += 1
        substrings.append("")
    
    return k, substrings

def main():
    # Read the input
    n = int(input())
    s = input()
    
    # Get the good substrings
    k, substrings = get_good_substrings(s)
    
    # Print the output
    print(k)
    print(" ".join(substrings))

if __name__ == '__main__':
    main()

