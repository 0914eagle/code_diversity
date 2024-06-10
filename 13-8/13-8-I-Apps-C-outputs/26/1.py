
import itertools

def get_complete_codes(partial_code):
    m, n = len(partial_code), len(partial_code[0])
    complete_codes = []
    for i in range(m):
        for j in range(n):
            if partial_code[i][j] == 0:
                continue
            for k in range(i+1, m):
                if partial_code[k][j] == 0:
                    continue
                for l in range(j+1, n):
                    if partial_code[i][l] == 0 or partial_code[k][l] == 0:
                        continue
                    complete_codes.append(list(itertools.product(partial_code[i][:j] + partial_code[k][j:l], partial_code[i][l:] + partial_code[k][l:])))
    return complete_codes

def count_complete_codes(partial_code):
    return len(get_complete_codes(partial_code))

if __name__ == '__main__':
    m, n = map(int, input().split())
    partial_code = []
    for _ in range(m):
        partial_code.append(list(map(int, input().split())))
    print(count_complete_codes(partial_code))

