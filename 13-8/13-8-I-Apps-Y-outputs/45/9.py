
def get_diverse_garland(s):
    n = len(s)
    recolored = 0
    t = [""] * n
    for i in range(n):
        if i > 0 and s[i] == s[i-1]:
            t[i] = "R" if s[i] == "G" else "G"
            recolored += 1
        else:
            t[i] = s[i]
    return recolored, "".join(t)

def main():
    n = int(input())
    s = input()
    recolored, t = get_diverse_garland(s)
    print(recolored)
    print(t)

if __name__ == '__main__':
    main()

