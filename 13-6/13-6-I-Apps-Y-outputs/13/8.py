
def is_palindrome(string):
    return string == string[::-1]

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def solve(string):
    num = int(string)
    if is_palindrome(string) and is_prime(num):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    string = input()
    print(solve(string))

