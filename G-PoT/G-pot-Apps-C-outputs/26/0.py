
n, x, y = map(int, input().split())
a = input().strip()

# Count the number of groups of consecutive zeros
groups = [len(group) for group in a.split('1') if group]

if not groups:
    print(0)
else:
    cost = (len(groups) - 1) * min(x, y) + y
    print(cost)
