
def get_carry_count(num1, num2):
    count = 0
    while num1 >= num2:
        count += 1
        num1 -= 1
        num2 += 1
    return count

def get_min_steps(num1, num2):
    carry_count = get_carry_count(num1, num2)
    return carry_count + 1

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(get_min_steps(num1, num2))

