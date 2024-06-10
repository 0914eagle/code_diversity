
def is_valid_divisibility_hack(b, d):
    if b == 1 or d == 1:
        return "yes"
    if b % d == 0 or d % b == 0:
        return "yes"
    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0 and d % i == 0:
            return "yes"
    return "no"

def main():
    b, d = map(int, input().split())
    print(is_valid_divisibility_hack(b, d))

if __name__ == '__main__':
    main()

