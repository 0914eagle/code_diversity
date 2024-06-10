
def get_original_task(numbers):
    original_task = ""
    for number in numbers:
        original_task += str(number) + "^"
    original_task = original_task[:-1]
    return original_task

def get_x_value(numbers):
    x_value = 0
    for number in numbers:
        x_value += number
    return x_value

def main():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    original_task = get_original_task(numbers)
    x_value = get_x_value(numbers)
    print(x_value)

if __name__ == '__main__':
    main()

