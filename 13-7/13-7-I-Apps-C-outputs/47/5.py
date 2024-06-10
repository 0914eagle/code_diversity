
def get_empty_squares(N):
    # Initialize variables
    empty_squares = 0
    widgets_packed = 0
    
    # Iterate through all possible box sizes
    for W in range(1, int(N**0.5) + 1):
        for H in range(W, 2*W):
            # Calculate the number of widgets that can be packed in the current box
            widgets_per_box = W * H
            
            # If the current box can fit all the widgets, calculate the number of empty squares and update the minimum
            if widgets_per_box >= N:
                empty_squares = (W * H) - N
                if empty_squares < min_empty_squares:
                    min_empty_squares = empty_squares
                    optimal_W = W
                    optimal_H = H
    
    # Return the minimum number of empty squares
    return min_empty_squares

def main():
    N = int(input())
    print(get_empty_squares(N))

if __name__ == '__main__':
    main()

