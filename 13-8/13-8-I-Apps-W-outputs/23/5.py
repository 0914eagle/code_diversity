
def solve(str1, str2):
    # Find all subpairs of str1 and str2
    subpairs_str1 = []
    subpairs_str2 = []
    for i in range(len(str1)):
        for j in range(len(str2)):
            subpairs_str1.append((str1[i:i+1], str2[j:j+1]))
            subpairs_str2.append((str1[i:i+1], str2[j:j+1]))
    
    # Find the maximum length palindrome by concatenating subpairs
    max_length = 0
    max_palindrome = ""
    for subpair1 in subpairs_str1:
        for subpair2 in subpairs_str2:
            concatenated = subpair1[0] + subpair1[1] + subpair2[0] + subpair2[1]
            if concatenated == concatenated[::-1] and len(concatenated) > max_length:
                max_length = len(concatenated)
                max_palindrome = concatenated
    
    return max_length

