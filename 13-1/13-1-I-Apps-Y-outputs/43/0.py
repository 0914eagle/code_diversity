
# Read input
A1, A2, A3 = map(int, input().split())

# Check if the sum is greater than or equal to 22
if A1 + A2 + A3 >= 22:
    print("bust")
else:
    print("win")

