
n, s = map(int, input().split())
volumes = list(map(int, input().split()))

# Sort the volumes in descending order
volumes.sort(reverse=True)

# Initialize the sum of the volumes
sum_volumes = 0

# Iterate through the volumes and check if the sum is greater than or equal to s
for i in range(n):
    sum_volumes += volumes[i]
    if sum_volumes >= s:
        print(volumes[i])
        break
else:
    print(-1)

