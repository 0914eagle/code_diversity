
def get_diverse_garland(s):
    n = len(s)
    recolored_lamp = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            recolored_lamp += 1
            if s[i] == 'R':
                s = s[:i] + 'G' + s[i+1:]
            elif s[i] == 'G':
                s = s[:i] + 'B' + s[i+1:]
            else:
                s = s[:i] + 'R' + s[i+1:]
    return recolored_lamp, s

def solve(s):
    n = len(s)
    recolored_lamp = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            recolored_lamp += 1
            if s[i] == 'R':
                s = s[:i] + 'G' + s[i+1:]
            elif s[i] == 'G':
                s = s[:i] + 'B' + s[i+1:]
            else:
                s = s[:i] + 'R' + s[i+1:]
    return recolored_lamp, s

if __name__ == '__main__':
    n = int(input())
    s = input()
    recolored_lamp, diverse_garland = solve(s)
    print(recolored_lamp)
    print(diverse_garland)

