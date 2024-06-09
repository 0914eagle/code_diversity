
def is_telephone_number(s):
    return len(s) == 11 and s[0] == '8'

def vasya_wins(n, s):
    count_8 = s.count('8')
    if count_8 <= n // 2:
        return "NO"
    else:
        return "YES"

n = int(input())
s = input()

print(vasya_wins(n, s))
