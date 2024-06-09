
n = int(input())
elements = list(map(int, input().split()))

neg_count = sum(1 for x in elements if x < 0)
if neg_count % 2 == 0 or n == 1:
    print(sum(abs(x) for x in elements))
else:
    min_abs = min(abs(x) for x in elements)
    print(sum(abs(x) for x in elements) - 2 * min_abs)
