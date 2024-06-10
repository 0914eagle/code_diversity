
def get_standard_sum(num1, num2):
    sum = 0
    while num1 > 0 or num2 > 0:
        sum += (num1 % 10) + (num2 % 10)
        num1 //= 10
        num2 //= 10
    return sum

def get_min_steps(num1, num2):
    steps = 0
    while get_standard_sum(num1, num2) > 9:
        steps += 1
        if num1 > num2:
            num1 -= 1
        else:
            num2 -= 1
    return steps

def main():
    num1, num2 = map(int, input().split())
    print(get_min_steps(num1, num2))

if __name__ == '__main__':
    main()

