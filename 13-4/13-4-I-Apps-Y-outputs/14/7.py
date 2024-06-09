
def get_marks(n):
    marks = {}
    for _ in range(n):
        name, *line = input().split()
        marks[name] = list(map(int, line))
    return marks

def get_average(marks, name):
    return sum(marks[name]) / len(marks[name])

def main():
    n = int(input())
    marks = get_marks(n)
    query_name = input()
    print(f"{get_average(marks, query_name):.2f}")

if __name__ == '__main__':
    main()

