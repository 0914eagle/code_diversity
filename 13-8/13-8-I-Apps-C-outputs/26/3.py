
import itertools

def get_complete_codes(partial_code):
    m, n = len(partial_code), len(partial_code[0])
    known_digits = set(itertools.chain(*partial_code)) - {0}
    possible_digits = set(range(1, 10)) - known_digits
    num_complete_codes = 0
    
    for assignment in itertools.product(possible_digits, repeat=len(known_digits)):
        code = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if partial_code[i][j] == 0:
                    code[i][j] = assignment[known_digits.index(partial_code[i][j-1]*partial_code[i-1][j])]
                else:
                    code[i][j] = partial_code[i][j]
        if is_valid_code(code):
            num_complete_codes += 1
    
    return num_complete_codes

def is_valid_code(code):
    m, n = len(code), len(code[0])
    for i in range(m):
        for j in range(n):
            if code[i][j] == 0:
                return False
            if i > 0 and code[i][j] == code[i-1][j]:
                return False
            if j > 0 and code[i][j] == code[i][j-1]:
                return False
    
    for i in range(m):
        for j in range(n):
            if i < m-1 and j < n-1:
                u, r = code[i][j], code[i][j+1]
                l, d = code[i+1][j], code[i+1][j+1]
                if u not in (l*r, l+r, l-r, l//r, r*l, r+l, r-l, r//l):
                    return False
    
    return True

def main():
    m, n = map(int, input().split())
    partial_code = []
    for _ in range(m):
        partial_code.append(list(map(int, input().split())))
    print(get_complete_codes(partial_code))

if __name__ == '__main__':
    main()

