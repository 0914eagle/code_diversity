
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
    
    # Find the maximum palindrome length and the corresponding subpairs
    max_len = 0
    max_subpairs = []
    for subpair1 in subpairs1:
        for subpair2 in subpairs2:
            x = subpair1[0] + subpair1[1] + subpair2[0] + subpair2[1]
            if x == x[::-1] and len(x) > max_len and len(subpair1[0]) == len(subpair2[0]) and len(subpair1[1]) == len(subpair2[1]):
                max_len = len(x)
                max_subpairs = [subpair1, subpair2]
    
    return max_len

