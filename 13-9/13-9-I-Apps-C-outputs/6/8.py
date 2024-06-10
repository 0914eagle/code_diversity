
def divisibility_hack(b, d):
    if b == 1 or d == 1:
        return "yes"
    if b % d == 0 or d % b == 0:
        return "yes"
    for m in range(1, b):
        if (b**m - 1) % d == 0:
            return "yes"
    return "no"

def main():
    b, d = map(int, input().split())
    print(divisibility_hack(b, d))

if __name__ == '__main__':
    main()

