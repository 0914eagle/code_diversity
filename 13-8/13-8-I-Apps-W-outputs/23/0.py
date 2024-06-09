
def solve(str1, str2):
    # Find all subpairs of str1 and str2
    subpairs1 = []
    subpairs2 = []
    for i in range(len(str1)):
        for j in range(i+1, len(str1)+1):
            subpairs1.append((str1[i:j], str1[j:]))
    for i in range(len(str2)):
        for j in range(i+1, len(str2)+1):
            subpairs2.append((str2[i:j], str2[j:]))
    
    # Find the maximum palindrome by iterating through all possible combinations of subpairs
    max_palindrome = 0
    for subpair1 in subpairs1:
        for subpair2 in subpairs2:
            concatenated = subpair1[0] + subpair1[1] + subpair2[0] + subpair2[1]
            if concatenated == concatenated[::-1] and len(concatenated) > max_palindrome:
                max_palindrome = len(concatenated)
    
    return max_palindrome

