
def get_different_string(s1, s2, t):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if t == 0:
                return s1[:i] + "a" + s1[i+1:]
            else:
                t -= 1
    return "-1"

def main():
    n, t = map(int, input().split())
    s1 = input()
    s2 = input()
    print(get_different_string(s1, s2, t))

if __name__ == '__main__':
    main()

