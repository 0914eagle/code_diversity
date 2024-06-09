
def is_phone_number(s):
    if len(s) != 11:
        return False
    if s[0] != "8":
        return False
    for i in range(1, 11):
        if not s[i].isdigit():
            return False
    return True

def make_phone_numbers(s):
    phone_numbers = []
    for i in range(len(s) - 10):
        if is_phone_number(s[i:i+11]):
            phone_numbers.append(s[i:i+11])
    return phone_numbers

def f1(n, s):
    return len(make_phone_numbers(s))

def f2(n, s):
    return 0

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))

