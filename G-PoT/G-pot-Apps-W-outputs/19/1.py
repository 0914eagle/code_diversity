
n = int(input())

# Find the largest power of 2 that is less than or equal to n
max_power_of_2 = 1
while max_power_of_2 * 2 <= n:
    max_power_of_2 *= 2

# Calculate the maximum number of games the winner can participate in
if n == max_power_of_2:
    print(max_power_of_2 // 2)
else:
    print(n - max_power_of_2)
