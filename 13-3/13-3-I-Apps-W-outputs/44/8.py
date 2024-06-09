
n = int(input())

# Calculate the maximum height of the pyramid
max_height = 0
for i in range(1, n + 1):
    if (i * (i + 1)) // 2 <= n:
        max_height = i
    else:
        break

print(max_height)

