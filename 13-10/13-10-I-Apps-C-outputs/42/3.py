
def is_valid_arrangement(arrangement, R, C, a, b, c):
    for i in range(R):
        for j in range(C):
            if arrangement[i][j] == 'A' and (j > 0 and arrangement[i][j-1] == 'A' or i > 0 and arrangement[i-1][j] == 'A'):
                return False
    return True

def solve(R, C, a, b, c):
    if a + b + c > R * C:
        return "impossible"
    
    arrangement = [[' '] * C for _ in range(R)]
    arrangement[0][0] = 'A'
    a -= 1
    b -= 1
    c -= 1
    
    for i in range(1, R):
        for j in range(1, C):
            if arrangement[i-1][j-1] == 'A':
                if a > 0:
                    arrangement[i][j] = 'A'
                    a -= 1
                elif b > 0:
                    arrangement[i][j] = 'B'
                    b -= 1
                else:
                    arrangement[i][j] = 'C'
                    c -= 1
            elif arrangement[i-1][j-1] == 'B':
                if b > 0:
                    arrangement[i][j] = 'B'
                    b -= 1
                elif a > 0:
                    arrangement[i][j] = 'A'
                    a -= 1
                else:
                    arrangement[i][j] = 'C'
                    c -= 1
            else:
                if c > 0:
                    arrangement[i][j] = 'C'
                    c -= 1
                elif b > 0:
                    arrangement[i][j] = 'B'
                    b -= 1
                else:
                    arrangement[i][j] = 'A'
                    a -= 1
    
    if is_valid_arrangement(arrangement, R, C, a, b, c):
        return '\n'.join(''.join(row) for row in arrangement)
    else:
        return "impossible"

def main():
    R, C, a, b, c = map(int, input().split())
    print(solve(R, C, a, b, c))

if __name__ == '__main__':
    main()

