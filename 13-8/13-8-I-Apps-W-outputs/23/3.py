
def find_palindrome(str1, str2):
    # Find all subpairs of str1 and str2
    subpairs1 = []
    subpairs2 = []
    for i in range(len(str1)):
        for j in range(i+1, len(str1)+1):
            subpairs1.append((str1[i:j], str1[j:i-1:-1]))
    for i in range(len(str2)):
        for j in range(i+1, len(str2)+1):
            subpairs2.append((str2[i:j], str2[j:i-1:-1]))
    
    # Find the maximum length palindrome by iterating over all possible subpairs
    max_length = 0
    for subpair1 in subpairs1:
        for subpair2 in subpairs2:
            if subpair1[0] == subpair2[1] and subpair1[1] == subpair2[0]:
                length = len(subpair1[0]) + len(subpair2[0])
                if length > max_length:
                    max_length = length
    
    return max_length

