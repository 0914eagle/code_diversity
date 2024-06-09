
def f(s, t):
    return ''.join([t[ord(c) - ord('a')] for c in s])

def fk(s, t, k):
    return f(s, t) if k == 1 else fk(f(s, t), t, k - 1)

def main():
    s = input()
    t = [input() for _ in range(13)]
    k = int(input())
    m = int(input())
    ms = [int(input()) for _ in range(m)]
    p = fk(s, t, k)
    for m in ms:
        print(p[m - 1])

if __name__ == '__main__':
    main()

