e_sugoroku(N, M, S):
    # Initialize a queue to perform BFS
    queue = [(0, [])]  # (current square, sequence of numbers)
    
    # Initialize a set to keep track of visited squares
    visited = set()
    
    # Perform BFS
    while queue:
        current_square, current_sequence = queue.pop(0)
        
        if current_square == N:
            return current_sequence
        
        if current_square in visited:
            continue
        
        visited.add(current_square)
        
        for number in range(1, M + 1):
            next_square = current_square + number
            
            if next_square > N or S[next_square] == '1':
                continue
            
            queue.append((next_square, current_sequence + [number]))
    
    return -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    S = input().strip()
    
    result = solve_sugoroku(N, M, S)
    if result == -1:
        print(-1)
    else:
        print(*result)  # Print the sequence of numbers with spaces in between
