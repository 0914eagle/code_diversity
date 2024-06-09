
def solve_circle_dance(N, moves):
    result = [''] * N
    clockwise = []
    counterclockwise = []
    
    for i in range(N):
        if i + moves[i] < N:
            clockwise.append((i + moves[i], i))
        else:
            clockwise.append((i + moves[i] - N, i))
        
        if i - moves[i] >= 0:
            counterclockwise.append((i - moves[i], i))
        else:
            counterclockwise.append((i - moves[i] + N, i))
    
    clockwise.sort()
    counterclockwise.sort()
    
    for i in range(N):
        if clockwise[i][0] == i:
            result[clockwise[i][1]] = 'R'
        elif counterclockwise[i][0] == i:
            result[counterclockwise[i][1]] = 'L'
        else:
            return 'no dance'
    
    return ''.join(result)

# Input parsing
N = int(input())
moves = list(map(int, input().split()))

# Solve the problem
result = solve_circle_dance(N, moves)
print(result)
