
def get_carry_steps(num1, num2):
    # Initialize variables
    steps = 0
    carry = 0

    # Loop until there is no carry
    while carry != 0 or num1 < num2:
        # Add 1 to one number and subtract 1 from the other
        num1 += 1
        num2 -= 1

        # Check if there is a carry
        carry = num1 // 10
        num1 %= 10

        # Increment the step count
        steps += 1

    # Return the step count
    return steps

def get_sum(num1, num2):
    # Get the carry steps
    steps = get_carry_steps(num1, num2)

    # Add the numbers without carry
    sum = num1 + num2

    # Add the carry steps to the sum
    for _ in range(steps):
        sum += 10

    # Return the sum
    return sum

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_sum(num1, num2))

