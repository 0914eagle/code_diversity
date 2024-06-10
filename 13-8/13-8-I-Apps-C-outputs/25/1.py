
def get_longest_common_subsequence(strings):
    # Find the length of the longest common subsequence
    # of the first two strings
    lcs_len = len(get_longest_common_subsequence_helper(strings[0], strings[1]))
    
    # Iterate over the remaining strings
    for i in range(2, len(strings)):
        # Find the length of the longest common subsequence
        # of the current string and the previous strings
        lcs_len = max(lcs_len, len(get_longest_common_subsequence_helper(strings[i], strings[i-1])))
    
    return lcs_len

def get_longest_common_subsequence_helper(s1, s2):
    # Initialize the length of the longest common subsequence
    lcs = 0
    
    # Iterate over the characters of both strings
    for i in range(len(s1)):
        for j in range(len(s2)):
            # If the characters match, increment the length of the longest common subsequence
            if s1[i] == s2[j]:
                lcs += 1
    
    return lcs

def main():
    # Read the input data
    n, k = map(int, input().split())
    strings = []
    for i in range(n):
        strings.append(input())
    
    # Find the length of the longest common subsequence
    lcs_len = get_longest_common_subsequence(strings)
    
    # Print the result
    print(lcs_len)

if __name__ == '__main__':
    main()

