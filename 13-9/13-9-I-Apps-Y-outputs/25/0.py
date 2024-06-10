
def check_statement(matrix, a, b):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != a[i] + b[j]:
                return False
    return True

def input_data():
    matrix = []
    a = []
    b = []
    for i in range(3):
        matrix.append(list(map(int, input().split())))
        a.append(int(input()))
        b.append(int(input()))
    return matrix, a, b

def main():
    matrix, a, b = input_data()
    if check_statement(matrix, a, b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

