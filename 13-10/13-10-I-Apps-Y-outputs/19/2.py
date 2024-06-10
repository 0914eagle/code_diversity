
def get_median(s, t):
    k = len(s)
    strings = []
    for i in range(ord('a'), ord('a') + k):
        for j in range(ord('a'), ord('a') + k):
            if s <= chr(i) + chr(j) <= t:
                strings.append(chr(i) + chr(j))
    return sorted(strings)[len(strings) // 2]

def main():
    k = int(input())
    s = input()
    t = input()
    print(get_median(s, t))

if __name__ == '__main__':
    main()

