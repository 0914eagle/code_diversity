
def find_teleport_directions(N, moves):
    result = [''] * N
    for i in range(N):
        if i - moves[i] >= 0:
            result[i - moves[i]] = 'R'
        if i + moves[i] < N:
            result[i + moves[i]] = 'L'
    for i in range(N):
        if result[i] == '':
            return 'no dance'
    return ''.join(result)

# Input
N = int(input())
moves = list(map(int, input().split()))

# Output
print(find_teleport_directions(N, moves))
