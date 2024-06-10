
def get_diverse_garland(s):
    n = len(s)
    recolored_lamp_count = 0
    diverse_garland = ''
    for i in range(n):
        if i > 0 and s[i] == s[i-1]:
            recolored_lamp_count += 1
            if s[i] == 'R':
                diverse_garland += 'G'
            elif s[i] == 'G':
                diverse_garland += 'B'
            else:
                diverse_garland += 'R'
        else:
            diverse_garland += s[i]
    return recolored_lamp_count, diverse_garland

def solve(s):
    n = len(s)
    recolored_lamp_count = 0
    diverse_garland = ''
    for i in range(n):
        if i > 0 and s[i] == s[i-1]:
            recolored_lamp_count += 1
            if s[i] == 'R':
                diverse_garland += 'G'
            elif s[i] == 'G':
                diverse_garland += 'B'
            else:
                diverse_garland += 'R'
        else:
            diverse_garland += s[i]
    return recolored_lamp_count, diverse_garland

if __name__ == '__main__':
    n = int(input())
    s = input()
    recolored_lamp_count, diverse_garland = solve(s)
    print(recolored_lamp_count)
    print(diverse_garland)

