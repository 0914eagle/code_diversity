
from collections import namedtuple

def get_data(n):
    columns = input().split()
    data = []
    for _ in range(n):
        data.append(namedtuple('Data', columns)(*input().split()))
    return data

def calculate_average(data):
    total = 0
    for student in data:
        total += student.MARKS
    return total / len(data)

def main():
    n = int(input())
    data = get_data(n)
    average = calculate_average(data)
    print(f'{average:.2f}')

if __name__ == '__main__':
    main()

