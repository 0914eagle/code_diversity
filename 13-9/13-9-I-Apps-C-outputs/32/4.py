
def get_input():
    num1 = int(input())
    num2 = int(input())
    return num1, num2

def get_steps(num1, num2):
    steps = 0
    while num1 != num2:
        if num1 > num2:
            num1 -= 1
            steps += 1
        else:
            num2 -= 1
            steps += 1
    return steps

def get_output(num1, num2):
    steps = get_steps(num1, num2)
    return steps

if __name__ == '__main__':
    num1, num2 = get_input()
    output = get_output(num1, num2)
    print(output)

