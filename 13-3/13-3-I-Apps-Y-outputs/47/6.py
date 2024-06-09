
n, k = map(int, input().split())
d, s = map(int, input().split())

# Calculate the average difficulty of the solved problems
avg_solved = s * k / n

# Calculate the average difficulty of the unsolved problems
avg_unsolved = (d - avg_solved) * (n - k) / k

# Check if the average difficulty of the unsolved problems is possible
if avg_unsolved < 0 or avg_unsolved > 100:
    print("impossible")
else:
    print(f"{avg_unsolved:.6f}")

