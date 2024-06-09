
def get_max_candies(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c


q = int(input())

for i in range(q):
    a, b, c = map(int, input().split())
    print(get_max_candies(a, b, c))

