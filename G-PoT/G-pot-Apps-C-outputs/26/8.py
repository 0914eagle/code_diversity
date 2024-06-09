
n, x, y = map(int, input().split())
s = input().strip()

# Count the number of groups of consecutive zeros
groups = [len(group) for group in s.split('1') if group]

if not groups:
    print(0)
elif x <= y:
    print(x * (len(groups) - 1) + y)
else:
    print(y + x * (len(groups) - 1))
