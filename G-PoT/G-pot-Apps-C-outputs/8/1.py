
n = int(input())

# Function to check if a number is a power of 2
def is_power_of_2(num):
    return num != 0 and (num & (num - 1)) == 0

# Vasya wins if n is not a power of 2
if not is_power_of_2(n):
    print("Vasya")
else:
    print("Petya")
