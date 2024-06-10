
def divisibility_hack(b, d):
    if b == 1:
        return "yes"
    if d == 1:
        return "yes"
    if b == d:
        return "no"
    if b % d == 0:
        return "no"
    if d % b == 0:
        return "yes"
    for m in range(1, b):
        if (b * m) % d == 0:
            return "yes"
    return "no"

def main():
    b, d = map(int, input().split())
    print(divisibility_hack(b, d))

if __name__ == '__main__':
    main()

