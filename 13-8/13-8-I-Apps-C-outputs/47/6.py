
def get_carry_steps(num1, num2):
    steps = 0
    while num1 > num2:
        steps += 1
        num1 -= 1
        num2 += 1
    return steps

def get_min_steps(num1, num2):
    carry_steps = get_carry_steps(num1, num2)
    standard_steps = num1 + num2
    return min(carry_steps, standard_steps)

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_min_steps(num1, num2))

