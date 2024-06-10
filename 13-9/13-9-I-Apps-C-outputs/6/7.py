
def is_divisible(b, d):
    if b == 1:
        return "yes"
    if b == d:
        return "yes"
    if d % 2 == 0 and b % 2 == 0:
        return "no"
    if d % 5 == 0 and b % 5 == 0:
        return "no"
    for i in range(1, int(d ** 0.5) + 1):
        if d % i == 0 and b % i == 0:
            return "no"
    return "yes"

def main():
    b, d = map(int, input().split())
    print(is_divisible(b, d))

if __name__ == '__main__':
    main()

