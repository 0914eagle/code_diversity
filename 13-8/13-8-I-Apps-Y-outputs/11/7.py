
import collections
import sys

def get_input():
    N = int(input())
    columns = input().split()
    marks = []
    ids = []
    names = []
    classes = []
    for i in range(N):
        mark, id, name, cls = input().split()
        marks.append(int(mark))
        ids.append(int(id))
        names.append(name)
        classes.append(cls)
    return N, columns, marks, ids, names, classes

def solve(N, columns, marks, ids, names, classes):
    average = sum(marks) / N
    return round(average, 2)

def main():
    N, columns, marks, ids, names, classes = get_input()
    average = solve(N, columns, marks, ids, names, classes)
    print(average)

if __name__ == '__main__':
    main()

