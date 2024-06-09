
x = int(input())

# Convert the number to a string
x_str = str(x)

# Initialize the minimum number as the original number
min_num = x

# Iterate through each digit in the number
for i in range(len(x_str)):
    # Calculate the inverted digit
    inverted_digit = 9 - int(x_str[i])
    
    # Calculate the new number by replacing the current digit with the inverted digit
    new_num = int(x_str[:i] + str(inverted_digit) + x_str[i+1:])
    
    # If the new number is smaller than the minimum number, update the minimum number
    if new_num < min_num:
        min_num = new_num

print(min_num)

