
def get_carry_digits(num1, num2):
    carry_digits = 0
    while num1 >= 10 or num2 >= 10:
        carry_digits += 1
        num1 //= 10
        num2 //= 10
    return carry_digits

def get_min_steps(num1, num2):
    carry_digits = get_carry_digits(num1, num2)
    return carry_digits

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_min_steps(num1, num2))

