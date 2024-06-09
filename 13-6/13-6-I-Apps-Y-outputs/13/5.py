
def is_palindrome(string):
    return string == string[::-1]

def solve(string):
    if is_palindrome(string):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    string = input()
    print(solve(string))

