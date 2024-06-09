
def get_initial_chocolate_pieces(N, D, X, A):
    # Calculate the number of chocolate pieces eaten by each participant
    chocolate_pieces_eaten = [0] * N
    for i in range(N):
        chocolate_pieces_eaten[i] = (D - 1) // (A[i] + 1) + 1
    
    # Calculate the total number of chocolate pieces eaten
    total_chocolate_pieces_eaten = sum(chocolate_pieces_eaten)
    
    # Calculate the number of chocolate pieces prepared at the beginning of the camp
    initial_chocolate_pieces = X - total_chocolate_pieces_eaten
    
    return initial_chocolate_pieces

