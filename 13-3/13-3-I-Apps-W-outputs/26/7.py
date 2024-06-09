
def count_substring(string, substring, l, r):
    count = 0
    for i in range(l, r - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

n, m, q = map(int, input().split())
s = input()
t = input()

for i in range(q):
    l, r = map(int, input().split())
    print(count_substring(s, t, l, r))

