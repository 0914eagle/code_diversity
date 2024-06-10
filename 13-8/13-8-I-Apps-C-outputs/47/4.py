
def get_carry_count(num1, num2):
    count = 0
    while num1 > 0 and num2 > 0:
        if num1 + num2 > 9:
            count += 1
        num1 -= 1
        num2 += 1
    return count

def get_second_method_steps(num1, num2):
    count = 0
    while num1 > 0 and num2 > 0:
        if num1 + num2 > 9:
            count += 1
            num1 -= 1
            num2 += 1
        else:
            break
    return count

def get_min_steps(num1, num2):
    carry_count = get_carry_count(num1, num2)
    second_method_steps = get_second_method_steps(num1, num2)
    return min(carry_count, second_method_steps)

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_min_steps(num1, num2))

