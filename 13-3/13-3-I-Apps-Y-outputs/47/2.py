
n, k = map(int, input().split())
d, s = map(int, input().split())

# Calculate the average difficulty of the solved problems
solved_avg = s * k / n

# Calculate the average difficulty of the unsolved problems
unsolved_avg = (d - solved_avg) * (n - k) / k

# Check if the average difficulty of the unsolved problems exists
if unsolved_avg < 0 or unsolved_avg > 100:
    print("impossible")
else:
    print(round(unsolved_avg, 6))

