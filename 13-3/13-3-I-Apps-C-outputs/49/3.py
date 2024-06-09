
n = int(input())

# Initialize the maximum sum as 0
max_sum = 0

# Loop through all possible values of a
for a in range(n+1):
    # Find the corresponding value of b
    b = n - a
    
    # Calculate the sum of digits in a and b
    sum_a = sum(int(digit) for digit in str(a))
    sum_b = sum(int(digit) for digit in str(b))
    
    # Calculate the total sum
    total_sum = sum_a + sum_b
    
    # Check if the total sum is greater than the maximum sum
    if total_sum > max_sum:
        # If it is, update the maximum sum and the values of a and b
        max_sum = total_sum
        max_a = a
        max_b = b

# Print the maximum sum
print(max_sum)

