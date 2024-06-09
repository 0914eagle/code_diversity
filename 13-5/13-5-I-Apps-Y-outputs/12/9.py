
from collections import namedtuple

def get_data():
    n = int(input())
    columns = input().split()
    data = []
    for _ in range(n):
        data.append(namedtuple('Student', columns)(*input().split()))
    return data

def calculate_average(data):
    total = 0
    for student in data:
        total += student.MARKS
    return round(total / len(data), 2)

def main():
    data = get_data()
    average = calculate_average(data)
    print(average)

if __name__ == '__main__':
    main()

