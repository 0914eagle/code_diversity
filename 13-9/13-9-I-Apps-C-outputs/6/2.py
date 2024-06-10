
def divisibility_hack_valid(b, d):
    if b == 1 or d == 1:
        return "yes"
    if d > b:
        return "no"
    for m in range(1, b):
        if (b**m - 1) % d == 0:
            return "yes"
    return "no"

def main():
    b, d = map(int, input().split())
    print(divisibility_hack_valid(b, d))

if __name__ == '__main__':
    main()

