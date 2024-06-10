
def get_carry_digits(num1, num2):
    carry_digits = 0
    while num1 >= num2:
        carry_digits += 1
        num1 -= 1
        num2 += 1
    return carry_digits

def get_steps(num1, num2):
    carry_digits = get_carry_digits(num1, num2)
    return carry_digits

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_steps(num1, num2))

