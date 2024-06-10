
def get_min_pieces(A, B):
    # Calculate the minimum number of pieces needed to distribute to A guests
    min_pieces_A = A
    
    # Calculate the minimum number of pieces needed to distribute to B guests
    min_pieces_B = B
    
    # Return the minimum of the two calculations
    return min(min_pieces_A, min_pieces_B)

def main():
    # Read the input from stdin
    A, B = map(int, input().split())
    
    # Calculate the minimum number of pieces needed to distribute to either A or B guests
    min_pieces = get_min_pieces(A, B)
    
    # Print the result
    print(min_pieces)

if __name__ == '__main__':
    main()

