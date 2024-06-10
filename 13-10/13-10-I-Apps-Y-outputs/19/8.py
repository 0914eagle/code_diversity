
def get_median(s, t):
    k = len(s)
    lst = []
    for i in range(ord('a'), ord('z') + 1):
        for j in range(ord('a'), ord('z') + 1):
            if ord(s[0]) <= i <= ord(t[0]) and ord(s[1]) <= j <= ord(t[1]):
                lst.append(chr(i) + chr(j))
    lst.sort()
    return lst[len(lst) // 2]

def main():
    k = int(input())
    s = input()
    t = input()
    print(get_median(s, t))

if __name__ == '__main__':
    main()

