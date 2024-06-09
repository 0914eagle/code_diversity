
n, x, y = map(int, input().split())
a = input()

# Count the number of groups of consecutive zeros
groups = [len(group) for group in a.split('1') if group]

if not groups:
    print(0)
elif x <= y:
    print((len(groups) - 1) * x + y)
else:
    print((len(groups) - 1) * y + x)
