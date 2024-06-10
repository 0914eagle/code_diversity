
def get_possible_codes(m, n, partial_code):
    possible_codes = 0
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if is_valid_code(m, n, partial_code, i, j, k):
                    possible_codes += 1
    return possible_codes

def is_valid_code(m, n, partial_code, i, j, k):
    for row in range(m):
        if partial_code[row][0] == i and partial_code[row][1] == j and partial_code[row][2] == k:
            return False
    for col in range(n):
        if partial_code[0][col] == i and partial_code[1][col] == j and partial_code[2][col] == k:
            return False
    for row in range(m - 1):
        for col in range(n - 1):
            if partial_code[row][col] == i and partial_code[row + 1][col] == j and partial_code[row][col + 1] == k:
                return False
    return True

def main():
    m, n = map(int, input().split())
    partial_code = []
    for _ in range(m):
        partial_code.append(list(map(int, input().split())))
    possible_codes = get_possible_codes(m, n, partial_code)
    print(possible_codes)

if __name__ == '__main__':
    main()

