
def get_diverse_garland(s):
    n = len(s)
    recolors = 0
    t = ""
    for i in range(n):
        if i > 0 and s[i] == s[i-1]:
            recolors += 1
            if s[i] == "R":
                t += "G"
            elif s[i] == "G":
                t += "B"
            else:
                t += "R"
        else:
            t += s[i]
    return recolors, t

def main():
    n = int(input())
    s = input()
    recolors, t = get_diverse_garland(s)
    print(recolors)
    print(t)

if __name__ == '__main__':
    main()

