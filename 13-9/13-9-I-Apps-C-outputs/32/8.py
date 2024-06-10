
def get_carry_digits(num1, num2):
    carry_digits = 0
    while num1 > 0 and num2 > 0:
        carry_digits += 1
        num1, num2 = num1 - 1, num2 - 1
    return carry_digits

def get_steps(num1, num2):
    steps = 0
    while num1 > 0 and num2 > 0:
        carry_digits = get_carry_digits(num1, num2)
        if carry_digits == 0:
            break
        steps += 1
        num1, num2 = num1 - 1, num2 - 1
    return steps

if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    print(get_steps(num1, num2))

