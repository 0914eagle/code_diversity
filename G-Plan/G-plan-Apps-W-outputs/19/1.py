
from collections import deque

def shortest_sequence_to_win(N, M, S):
    queue = deque([(0, [])])
    visited = set()
    
    while queue:
        current_square, sequence = queue.popleft()
        
        if current_square == N:
            return sequence
        
        if current_square in visited:
            continue
        
        visited.add(current_square)
        
        for i in range(1, M + 1):
            next_square = current_square + i
            if next_square <= N and S[next_square] == '0':
                queue.append((next_square, sequence + [i]))
    
    return None

if __name__ == "__main__":
    N, M = map(int, input().split())
    S = input().strip()
    
    result = shortest_sequence_to_win(N, M, S)
    if result is not None:
        print(*result)
    else:
        print(-1)
