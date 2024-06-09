
n = int(input())

# Initialize the maximum sum as 0
max_sum = 0

# Loop through all possible values of a
for a in range(n+1):
    # Find the value of b that satisfies a + b = n
    b = n - a
    
    # Calculate the sum of digits in a and b
    sum_a = sum(int(digit) for digit in str(a))
    sum_b = sum(int(digit) for digit in str(b))
    
    # Calculate the total sum
    total_sum = sum_a + sum_b
    
    # If the total sum is greater than the maximum sum, update the maximum sum
    if total_sum > max_sum:
        max_sum = total_sum

print(max_sum)

