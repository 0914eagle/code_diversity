
def get_carry_digits(num1, num2):
    carry_digits = 0
    while num1 >= 10 or num2 >= 10:
        carry_digits += 1
        num1 = num1 // 10
        num2 = num2 // 10
    return carry_digits

def get_steps(num1, num2):
    carry_digits = get_carry_digits(num1, num2)
    steps = 0
    while carry_digits > 0:
        steps += 1
        carry_digits -= 1
    return steps

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_steps(num1, num2))

