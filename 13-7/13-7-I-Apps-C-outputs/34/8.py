
def get_sum_using_standard_algorithm(num1, num2):
    sum = 0
    carry = 0
    while num1 > 0 or num2 > 0:
        sum = (num1 % 10) + (num2 % 10) + carry
        if sum > 9:
            carry = 1
            sum -= 10
        else:
            carry = 0
        num1 //= 10
        num2 //= 10
    return sum

def get_number_of_steps_to_add(num1, num2):
    count = 0
    while get_sum_using_standard_algorithm(num1, num2) > 9:
        count += 1
        if num1 > num2:
            num1 -= 1
        else:
            num2 -= 1
    return count

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_number_of_steps_to_add(num1, num2))

