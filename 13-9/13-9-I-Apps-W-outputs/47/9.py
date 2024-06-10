
def is_palindrome(s):
    return s == s[::-1]

def convert_string(s):
    original_string = ""
    while s != "":
        if s[0].isdigit():
            count = int(s[0])
            s = s[1:]
            while count > 0:
                original_string += s[:s.index("-")+1]
                count -= 1
                s = s[s.index("-")+1:]
        else:
            original_string += s[:s.index("-")+1]
            s = s[s.index("-")+1:]
    return original_string

def solve(s):
    original_string = convert_string(s)
    if is_palindrome(original_string):
        return "Return"
    else:
        return "Continue"

if __name__ == '__main__':
    s = input()
    print(solve(s))

