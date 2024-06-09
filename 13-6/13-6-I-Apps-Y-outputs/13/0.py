
def is_palindrome(s):
    return s == s[::-1]

def solve(s):
    if len(s) < 2:
        return "Yes"
    if is_palindrome(s):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    s = input()
    print(solve(s))

