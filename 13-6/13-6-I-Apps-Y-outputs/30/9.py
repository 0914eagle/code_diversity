
def get_mean(r1, r2):
    return (r1 + r2) / 2

def get_r2(r1, s):
    r2 = s * 2 - r1
    return r2

def main():
    r1, s = map(int, input().split())
    r2 = get_r2(r1, s)
    print(r2)

if __name__ == '__main__':
    main()

