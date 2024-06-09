
def solve(A, B):
    # Find the first occurrence of the shared letter in A and B
    shared_letter = next((letter for letter in A if letter in B), None)
    
    # If there is no shared letter, return an empty grid
    if not shared_letter:
        return []
    
    # Find the index of the shared letter in A
    shared_letter_index = A.index(shared_letter)
    
    # Create a grid with the correct dimensions
    grid = ['.' * len(A) for _ in range(len(B))]
    
    # Fill in the grid with the words A and B
    for i in range(len(B)):
        grid[i] = grid[i][:shared_letter_index] + A[shared_letter_index] + grid[i][shared_letter_index + 1:]
        grid[i] = grid[i][:shared_letter_index] + B[i] + grid[i][shared_letter_index + 1:]
    
    return grid

