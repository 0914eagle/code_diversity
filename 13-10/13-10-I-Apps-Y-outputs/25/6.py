
def aoramitch(n, p, s, v):
    c = (n * (log(n)**(1.5)) / (p * 1000000000)) ** (1/v)
    t = s * (1 + 1/c) / v
    return t, c

def main():
    n, p, s, v = map(float, input().split())
    t, c = aoramitch(n, p, s, v)
    print(t, c)

if __name__ == '__main__':
    main()

