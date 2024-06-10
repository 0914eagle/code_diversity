
def find_good_strings(s):
    # Initialize a list to store the good strings
    good_strings = []
    
    # Iterate through the string and check if each substring is good
    for i in range(len(s)):
        # If the substring is good, add it to the list of good strings
        if is_good_string(s[i:]):
            good_strings.append(s[i:])
            break
    
    # If there are no good strings, return an empty list
    if not good_strings:
        return []
    
    # Initialize a list to store the final good strings
    final_good_strings = []
    
    # Iterate through the list of good strings and check if they can be combined to form the original string
    for i in range(len(good_strings)):
        # If the concatenation of the good strings is equal to the original string, add them to the final list of good strings
        if "".join(good_strings[:i+1]) == s:
            final_good_strings.append("".join(good_strings[:i+1]))
    
    # Return the final list of good strings
    return final_good_strings

def is_good_string(s):
    # Check if the string has an equal number of zeros and ones
    if s.count("0") == s.count("1"):
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input())
    s = input()
    good_strings = find_good_strings(s)
    print(len(good_strings))
    print(" ".join(good_strings))

