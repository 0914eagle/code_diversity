
def get_steps_standard_method(num1, num2):
    steps = 0
    while num1 > 0 and num2 > 0:
        if num1 % 10 + num2 % 10 > 9:
            steps += 1
        num1 //= 10
        num2 //= 10
    return steps

def get_steps_carry_method(num1, num2):
    steps = 0
    while num1 > 0 and num2 > 0:
        if num1 % 10 + num2 % 10 > 9:
            steps += 1
            num1 -= 1
            num2 += 1
        num1 //= 10
        num2 //= 10
    return steps

def get_min_steps(num1, num2):
    return min(get_steps_standard_method(num1, num2), get_steps_carry_method(num1, num2))

if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    print(get_min_steps(num1, num2))

