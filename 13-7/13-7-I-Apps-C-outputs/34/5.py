
def get_carry_digits(num1, num2):
    carry_digits = 0
    while num1 > 0 and num2 > 0:
        if num1 % 10 + num2 % 10 > 9:
            carry_digits += 1
        num1 //= 10
        num2 //= 10
    return carry_digits

def get_steps(num1, num2):
    steps = 0
    while get_carry_digits(num1, num2) > 0:
        steps += 1
        if num1 > num2:
            num1 -= 1
        else:
            num2 -= 1
    return steps

if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    print(get_steps(num1, num2))

