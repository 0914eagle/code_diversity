
def standard_addition(num1, num2):
    sum = 0
    carry = 0
    while num1 > 0 or num2 > 0:
        sum = (num1 % 10) + (num2 % 10) + carry
        carry = sum // 10
        num1 //= 10
        num2 //= 10
    return sum

def simple_addition(num1, num2):
    count = 0
    while num1 > num2:
        num1 -= 1
        num2 += 1
        count += 1
    return count

def combined_addition(num1, num2):
    count = 0
    while standard_addition(num1, num2) >= 10:
        num1 += 1
        num2 -= 1
        count += 1
    return count

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(combined_addition(num1, num2))

