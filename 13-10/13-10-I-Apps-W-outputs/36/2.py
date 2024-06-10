
def get_liked_string(s):
    # Check if the string contains "one" or "two" as a substring
    if "one" in s or "two" in s:
        return "0"
    
    # Check if the string contains "oneone" or "twoo" as a substring
    if "oneone" in s or "twoo" in s:
        return "1"
    
    # Check if the string contains "oneoneone" or "twooo" as a substring
    if "oneoneone" in s or "twooo" in s:
        return "2"
    
    # Check if the string contains "oneoneoneone" or "twoooo" as a substring
    if "oneoneoneone" in s or "twoooo" in s:
        return "3"
    
    # If none of the above conditions are met, the string is liked
    return "4"

def get_removed_indices(s):
    # Check if the string is liked
    if get_liked_string(s) == "0":
        return "0"
    
    # If the string is not liked, find the indices of the letters to remove
    indices = []
    for i in range(len(s)):
        if s[i] == "o" or s[i] == "t":
            indices.append(i)
    
    # Return the indices
    return " ".join(map(str, indices))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(get_liked_string(s))
        print(get_removed_indices(s))

