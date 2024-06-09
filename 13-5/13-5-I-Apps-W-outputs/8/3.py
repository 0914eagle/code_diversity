
def get_sum(matrix, row, col):
    
    sum = 0
    for i in range(len(matrix)):
        if i == row:
            sum += matrix[i][col]
        elif col == row:
            sum += matrix[i][col]
    return sum

def get_max_sum(matrix, pairs):
    
    max_sum = 0
    for pair in pairs:
        row, col = pair
        sum = get_sum(matrix, row, col)
        if sum > max_sum:
            max_sum = sum
    return max_sum

def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    l = int(input())
    pairs = []
    for i in range(l):
        pairs.append(list(map(int, input().split())))
    print(get_max_sum(matrix, pairs))

if __name__ == '__main__':
    main()

