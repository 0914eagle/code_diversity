
n = int(input())
p = list(map(int, input().split()))

# Calculate the deviation of the permutation
dev = sum(abs(p[i] - i) for i in range(n))

# Find the minimum deviation of cyclic shifts
min_dev = dev
min_id = 0
for i in range(n):
    dev = sum(abs(p[i+j] - (i+j)%n) for j in range(n))
    if dev < min_dev:
        min_dev = dev
        min_id = i

print(min_dev, min_id)

