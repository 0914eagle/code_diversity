
def get_input():
    n, m = map(int, input().split())
    pairs = []
    for i in range(m):
        a, b = map(int, input().split())
        pairs.append((a, b))
    return n, m, pairs

def check_pairs(pairs):
    x = 1
    while x <= n:
        y = x + 1
        while y <= n:
            found = False
            for a, b in pairs:
                if a == x or b == x or a == y or b == y:
                    found = True
                    break
            if found:
                return "YES"
            y += 1
        x += 1
    return "NO"

def main():
    n, m, pairs = get_input()
    print(check_pairs(pairs))

if __name__ == '__main__':
    main()

