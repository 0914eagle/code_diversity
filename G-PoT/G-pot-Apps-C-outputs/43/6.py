
def find_teleport_directions(N, moves):
    teleport_directions = [''] * N
    for i in range(N):
        if i % 2 == 0:
            teleport_directions[i] = 'L'
        else:
            teleport_directions[i] = 'R'
    
    for i in range(N):
        if teleport_directions[i] == 'L':
            moves[i] = (moves[i] + i) % N
        else:
            moves[i] = (i - moves[i] + N) % N
    
    positions = [0] * N
    for i in range(N):
        if positions[moves[i]] != 0:
            return "no dance"
        positions[moves[i]] = i + 1
    
    return ''.join(teleport_directions)

# Read input
N = int(input())
moves = list(map(int, input().split()))

# Find teleport directions
result = find_teleport_directions(N, moves)
print(result)
