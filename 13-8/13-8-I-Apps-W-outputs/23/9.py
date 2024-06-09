
def is_palindrome(string):
    return string == string[::-1]

def get_max_palindrome_subpair(str1, str2):
    for i in range(len(str1)):
        for j in range(len(str2)):
            if is_palindrome(str1[i:] + str2[:j]):
                return len(str1[i:]) + len(str2[:j])
    return 0

def solve(str1, str2):
    return get_max_palindrome_subpair(str1, str2)

