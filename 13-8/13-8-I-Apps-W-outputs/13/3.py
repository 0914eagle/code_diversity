
def cut_string(s):
    # Initialize variables
    k = 0
    s_list = []
    
    # Loop through the string and check if each substring is good
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_good(s[i:j]):
                s_list.append(s[i:j])
                k += 1
    
    # Return the minimum number of strings and the list of good substrings
    return k, s_list

def is_good(s):
    # Check if the string has an equal number of zeros and ones
    if s.count("0") == s.count("1"):
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input())
    s = input()
    k, s_list = cut_string(s)
    print(k)
    for i in range(k):
        print(s_list[i], end=" ")

