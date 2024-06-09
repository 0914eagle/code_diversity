
def check_pairs(pairs):
    x = 1
    while x <= n:
        y = x + 1
        while y <= n:
            found = False
            for pair in pairs:
                if x in pair or y in pair:
                    found = True
                    break
            if not found:
                return "NO"
            y += 1
        x += 1
    return "YES"

def main():
    n, m = map(int, input().split())
    pairs = []
    for i in range(m):
        a, b = map(int, input().split())
        pairs.append((a, b))
    print(check_pairs(pairs))

if __name__ == '__main__':
    main()

