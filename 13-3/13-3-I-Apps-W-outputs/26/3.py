
def count_occurrences(s, t, l, r):
    count = 0
    for i in range(l, r + 1):
        if s[i:i+len(t)] == t:
            count += 1
    return count

n, m, q = map(int, input().split())
s = input()
t = input()

for i in range(q):
    l, r = map(int, input().split())
    print(count_occurrences(s, t, l, r))

