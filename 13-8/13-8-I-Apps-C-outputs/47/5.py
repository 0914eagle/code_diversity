
def standard_addition(num1, num2):
    sum = 0
    carry = 0
    while num1 > 0 or num2 > 0:
        sum = (num1 % 10) + (num2 % 10) + carry
        carry = sum // 10
        num1 = num1 // 10
        num2 = num2 // 10
    return sum

def faster_addition(num1, num2):
    while num1 >= num2:
        num1 -= 1
        num2 += 1
    return num1 + num2

if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    print(faster_addition(num1, num2))

