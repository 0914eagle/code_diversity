
def check_pairs(pairs):
    n = len(pairs)
    for i in range(n):
        for j in range(i+1, n):
            if pairs[i][0] == pairs[j][0] or pairs[i][1] == pairs[j][1]:
                return True
    return False

def find_xy(n, m, pairs):
    for x in range(1, n+1):
        for y in range(x+1, n+1):
            if check_pairs(pairs):
                return "YES"
    return "NO"

if __name__ == '__main__':
    n, m = map(int, input().split())
    pairs = []
    for i in range(m):
        a, b = map(int, input().split())
        pairs.append((a, b))
    print(find_xy(n, m, pairs))

