
# Read the input
N = int(input())
costs = [int(input()) for _ in range(N)]

# Calculate and output the number of digits for each estimated cost
for cost in costs:
    num_digits = len(str(cost))
    print(num_digits)
