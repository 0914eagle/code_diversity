
# Read input
A1, A2, A3 = map(int, input().split())

# Calculate the sum
sum = A1 + A2 + A3

# Check if the sum is greater than or equal to 22
if sum >= 22:
    print("bust")
else:
    print("win")

