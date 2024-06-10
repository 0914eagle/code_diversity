
def divisibility_hack(b, d):
    if b == 1 or d == 1:
        return "no"
    for m in range(1, b):
        if pow(b, m, d) == 1:
            return "yes"
    return "no"

def main():
    b, d = map(int, input().split())
    print(divisibility_hack(b, d))

if __name__ == '__main__':
    main()

