
def get_marks(name):
    marks = {}
    for _ in range(int(input())):
        name, *line = input().split()
        marks[name] = list(map(float, line))
    return marks

def get_average(marks, name):
    return sum(marks[name]) / len(marks[name])

def main():
    marks = get_marks(input())
    query_name = input()
    print(f"{get_average(marks, query_name):.2f}")

if __name__ == '__main__':
    main()

