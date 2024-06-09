
n, k = map(int, input().split())
difficulties = list(map(int, input().split()))

left = 0
right = n - 1
solved = 0

while left <= right:
    if difficulties[left] <= k:
        solved += 1
        difficulties.pop(left)
        n -= 1
    elif difficulties[right] <= k:
        solved += 1
        difficulties.pop(right)
        n -= 1
    else:
        break

print(solved)

