
def get_steps_standard_algorithm(num1, num2):
    steps = 0
    while num1 >= num2:
        num1 -= 1
        steps += 1
        if num1 < num2:
            break
    return steps

def get_steps_repeated_addition(num1, num2):
    steps = 0
    while num1 > 0 and num2 > 0:
        num1 -= 1
        num2 -= 1
        steps += 1
    return steps

def get_min_steps(num1, num2):
    steps_standard_algorithm = get_steps_standard_algorithm(num1, num2)
    steps_repeated_addition = get_steps_repeated_addition(num1, num2)
    return min(steps_standard_algorithm, steps_repeated_addition)

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_min_steps(num1, num2))

