
def is_telephone_number(s):
    if len(s) != 11:
        return False
    if s[0] != "8":
        return False
    for i in range(1, 11):
        if s[i].isdigit() == False:
            return False
    return True

def has_winning_strategy(s):
    if len(s) == 1:
        return True
    if len(s) == 11 and is_telephone_number(s):
        return True
    for i in range(len(s)):
        if has_winning_strategy(s[:i] + s[i+1:]):
            return True
    return False

if __name__ == '__main__':
    n = int(input())
    s = input()
    if has_winning_strategy(s):
        print("YES")
    else:
        print("NO")

