
def get_substring_count(t, s):
    count = 0
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            count += 1
    return count

def solve(n, k, t):
    s = ""
    while len(s) < k * n:
        s += t
    return s[:k * n]

if __name__ == '__main__':
    n, k = map(int, input().split())
    t = input()
    print(solve(n, k, t))

