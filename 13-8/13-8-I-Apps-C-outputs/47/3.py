
def add_positive_integers(num1, num2):
    carry = 0
    sum = 0
    while num1 > 0 or num2 > 0 or carry > 0:
        sum = (num1 % 10) + (num2 % 10) + carry
        carry = 0
        if sum >= 10:
            carry = 1
            sum -= 10
        num1 //= 10
        num2 //= 10
    return sum

def get_min_steps(num1, num2):
    steps = 0
    while num1 > 0 and num2 > 0:
        sum = add_positive_integers(num1, num2)
        if sum >= 10:
            steps += 1
            num1 -= 1
        else:
            break
    return steps

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_min_steps(num1, num2))

