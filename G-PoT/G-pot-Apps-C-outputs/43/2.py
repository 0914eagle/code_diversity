
def find_teleport_directions(N, moves):
    result = [''] * N
    for i in range(N):
        if i % 2 == 0:
            result[i] = 'L'
        else:
            result[i] = 'R'
    
    for i in range(N):
        if result[i] == 'L':
            moves[i] = (moves[i] + i) % N
        else:
            moves[i] = (moves[i] - i + N) % N
    
    for i in range(N):
        if moves[i] != i:
            return "no dance"
    
    return ''.join(result)

# Read input
N = int(input())
moves = list(map(int, input().split()))

# Call the function and print the result
print(find_teleport_directions(N, moves))
