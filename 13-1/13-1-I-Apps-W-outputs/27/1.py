
def is_palindrome(s):
    return s == s[::-1]

def first_wins(s):
    if len(s) == 1:
        return True
    for i in range(len(s)):
        if is_palindrome(s[:i] + s[i+1:]):
            return True
    return False

def second_wins(s):
    if len(s) == 1:
        return False
    for i in range(len(s)):
        if is_palindrome(s[:i] + s[i+1:]):
            return False
    return True

def main():
    s = input()
    if first_wins(s):
        print("First")
    else:
        print("Second")

if __name__ == '__main__':
    main()

