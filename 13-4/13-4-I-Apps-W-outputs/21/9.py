
def is_palindrome(s):
    return s == s[::-1]

def get_good_string(s):
    if is_palindrome(s):
        return "-1"
    else:
        return "".join(sorted(s))

t = int(input())
for _ in range(t):
    s = input()
    print(get_good_string(s))

