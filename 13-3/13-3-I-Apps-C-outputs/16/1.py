
n, m = map(int, input().split())

users = set()
leaders = set()

for i in range(m):
    user, status = input().split()
    user = int(user[1:])
    if status == "+":
        users.add(user)
        if len(users) == 1:
            leaders.add(user)
    else:
        users.remove(user)
        if len(users) == 0:
            leaders.remove(user)

print(len(leaders))
if leaders:
    print(*sorted(leaders), sep=" ")
else:
    print(0)

