
def get_original_task(n, powers, numbers):
    task = ""
    for i in range(n):
        task += str(numbers[i]) + "^" + str(powers[i]) + " + "
    task = task[:-3]
    return task

def calculate_x(task):
    x = 0
    for term in task.split("+"):
        x += int(term)
    return x

def main():
    n = int(input())
    powers = []
    numbers = []
    for i in range(n):
        powers.append(int(input()))
        numbers.append(int(input()))
    task = get_original_task(n, powers, numbers)
    x = calculate_x(task)
    print(x)

if __name__ == '__main__':
    main()

