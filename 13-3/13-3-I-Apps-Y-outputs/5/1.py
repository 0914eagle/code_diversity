
def is_sorted(s):
    return s == ''.join(sorted(s))

def get_coloring(s):
    n = len(s)
    coloring = [0] * n
    for i in range(n):
        if s[i] == 'a':
            coloring[i] = 0
        elif s[i] == 'b':
            coloring[i] = 1
        else:
            return "NO"
    return "YES\n" + ''.join(map(str, coloring))

n = int(input())
s = input()
if is_sorted(s):
    print("YES")
    print("0" * n)
else:
    print(get_coloring(s))

