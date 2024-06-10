
def get_carry_steps(num1, num2):
    # Initialize variables
    carry_steps = 0
    num1_temp = num1
    num2_temp = num2

    # Repeat until there is no carry digit
    while num1_temp + num2_temp >= 10:
        carry_steps += 1
        num1_temp -= 1
        num2_temp += 1

    return carry_steps

def get_min_steps(num1, num2):
    # Get the carry steps using the second method
    carry_steps = get_carry_steps(num1, num2)

    # Get the minimum number of steps using the first method
    min_steps = 0
    while num1 + num2 >= 10:
        min_steps += 1
        num1 -= 1
        num2 += 1

    # Return the minimum number of steps
    return min_steps + carry_steps

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_min_steps(num1, num2))

