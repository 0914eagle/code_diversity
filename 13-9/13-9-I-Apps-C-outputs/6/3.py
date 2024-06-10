
def is_divisibility_hack_valid(b, d):
    if b == 1 or d == 1:
        return True
    if b % d == 0 or d % b == 0:
        return False
    for m in range(1, b):
        if (b ** m - 1) % d == 0:
            return True
    return False

def main():
    b, d = map(int, input().split())
    print("yes") if is_divisibility_hack_valid(b, d) else print("no")

if __name__ == '__main__':
    main()

