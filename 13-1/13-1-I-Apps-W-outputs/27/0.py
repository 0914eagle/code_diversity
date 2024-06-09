
def is_palindrome(s):
    return s == s[::-1]

def first_wins(s):
    if len(s) % 2 == 0:
        return is_palindrome(s[:len(s)//2])
    else:
        return is_palindrome(s[:len(s)//2]) or is_palindrome(s[len(s)//2+1:])

def second_wins(s):
    if len(s) % 2 == 0:
        return is_palindrome(s[len(s)//2:])
    else:
        return is_palindrome(s[:len(s)//2]) and is_palindrome(s[len(s)//2+1:])

def main():
    s = input()
    if first_wins(s):
        print("First")
    elif second_wins(s):
        print("Second")
    else:
        print("Draw")

if __name__ == '__main__':
    main()

