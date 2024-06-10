
def get_complete_codes(partial_code):
    m, n = len(partial_code), len(partial_code[0])
    complete_codes = 0
    for i in range(m):
        for j in range(n):
            if partial_code[i][j] == 0:
                continue
            for k in range(i, m):
                for l in range(j, n):
                    if partial_code[k][l] == 0:
                        continue
                    if partial_code[i][j] * partial_code[k][l] == partial_code[k][j]:
                        complete_codes += 1
                    if partial_code[i][j] + partial_code[k][l] == partial_code[k][j]:
                        complete_codes += 1
                    if partial_code[i][j] - partial_code[k][l] == partial_code[k][j] or partial_code[k][l] - partial_code[i][j] == partial_code[k][j]:
                        complete_codes += 1
                    if partial_code[i][j] // partial_code[k][l] == partial_code[k][j] or partial_code[k][l] // partial_code[i][j] == partial_code[k][j]:
                        complete_codes += 1
    return complete_codes

def main():
    m, n = map(int, input().split())
    partial_code = []
    for _ in range(m):
        partial_code.append(list(map(int, input().split())))
    print(get_complete_codes(partial_code))

if __name__ == '__main__':
    main()

