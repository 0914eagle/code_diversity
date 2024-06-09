
n = int(input())

# Initialize the maximum sum as 0
max_sum = 0

# Iterate from 1 to n
for a in range(1, n + 1):
    # Find the sum of digits in a
    sum_a = sum(int(digit) for digit in str(a))
    
    # Find the difference between n and a
    diff = n - a
    
    # Find the sum of digits in diff
    sum_diff = sum(int(digit) for digit in str(diff))
    
    # Calculate the total sum
    total_sum = sum_a + sum_diff
    
    # If the total sum is greater than the maximum sum, update the maximum sum
    if total_sum > max_sum:
        max_sum = total_sum

# Print the maximum sum
print(max_sum)

