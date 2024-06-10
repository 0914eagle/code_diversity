
def add_with_carry(num1, num2):
    carry = 0
    while num1 > 0 and num2 > 0:
        sum = num1 % 10 + num2 % 10 + carry
        if sum > 9:
            carry = 1
        else:
            carry = 0
        num1 //= 10
        num2 //= 10
    return carry

def add_two_numbers(num1, num2):
    steps = 0
    while add_with_carry(num1, num2) != 0:
        steps += 1
        if num1 > num2:
            num1 -= 1
        else:
            num2 -= 1
    return steps

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(add_two_numbers(num1, num2))

