
def get_antipalindromic_permutation(s):
    n = len(s)
    if n % 2 == 1:
        return None
    
    # create a dictionary to map each character to its index
    char_to_index = {}
    for i in range(n):
        char_to_index[s[i]] = i
    
    # create a list to store the permutation
    permutation = [0] * n
    
    # iterate through the characters of the input string
    for i in range(n):
        # find the index of the character in the permutation
        index = char_to_index[s[i]]
        
        # if the index is even, add the character to the permutation
        if index % 2 == 0:
            permutation[index] = s[i]
        # if the index is odd, add the character to the end of the permutation
        else:
            permutation[n - index] = s[i]
    
    return "".join(permutation)

def get_max_beauty(s, b):
    # get the antipalindromic permutation of the input string
    permutation = get_antipalindromic_permutation(s)
    if permutation is None:
        return 0
    
    # calculate the beauty of the permutation
    beauty = 0
    for i in range(len(s)):
        beauty += b[i] if permutation[i] == s[i] else 0
    
    return beauty

if __name__ == '__main__':
    n = int(input())
    s = input()
    b = list(map(int, input().split()))
    print(get_max_beauty(s, b))

