
def get_board_value(row, col):
    if col == 1:
        return row
    else:
        return get_board_value(row, col - 1) + get_board_value(row, col - 1)[::-1]

def solve(a, b):
    count = 0
    for i in range(a, b + 1):
        for j in range(1, get_board_value(i, 1) + 1):
            if get_board_value(i, j) == i:
                count += 1
    return count

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        a, b = map(int, input().split())
        print(solve(a, b))

