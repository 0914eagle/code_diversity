
def solve(str1, str2):
    # Find all subpairs of str1 and str2
    subpairs1 = []
    subpairs2 = []
    for i in range(len(str1)):
        for j in range(i+1, len(str1)+1):
            subpairs1.append((str1[i:j], str1[j:i-1:-1]))
    for i in range(len(str2)):
        for j in range(i+1, len(str2)+1):
            subpairs2.append((str2[i:j], str2[j:i-1:-1]))
    
    # Find the maximum length palindrome by iterating through all possible combinations of subpairs
    max_length = 0
    for pair1 in subpairs1:
        for pair2 in subpairs2:
            concat = pair1[0] + pair1[1] + pair2[0] + pair2[1]
            if (concat == concat[::-1]) and (len(concat) > max_length):
                max_length = len(concat)
    
    return max_length

