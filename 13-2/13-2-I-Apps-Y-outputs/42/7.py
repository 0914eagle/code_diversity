
import sys

# Read the input
N = int(input())
otoshidama = []
for i in range(N):
    x, u = input().split()
    if u == "JPY":
        otohashi = int(x)
    else:
        otohashi = float(x) * 380000.0
    otohashi.append(otohashi)

# Calculate the total value of the gifts
total_value = sum(otohashi)

# Print the total value
print(total_value)

