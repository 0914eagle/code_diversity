
def get_min_moves(a):
    # Find the starting and ending positions of the first and last book
    start, end = 0, 0
    for i in range(len(a)):
        if a[i] == 1:
            start = i
            break
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 1:
            end = i
            break
    
    # Initialize the minimum number of moves to 0
    min_moves = 0
    
    # Loop through the books and check if there are any gaps
    for i in range(start, end + 1):
        if a[i] == 0:
            # If there is a gap, find the nearest book to the left and right
            left, right = 0, 0
            for j in range(i - 1, -1, -1):
                if a[j] == 1:
                    left = j
                    break
            for j in range(i + 1, len(a)):
                if a[j] == 1:
                    right = j
                    break
            
            # Calculate the number of moves required to shift the segment to the left or right
            left_moves = i - left
            right_moves = right - i
            
            # Update the minimum number of moves if necessary
            if left_moves < right_moves:
                min_moves += left_moves
            else:
                min_moves += right_moves
    
    return min_moves

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_min_moves(a))

if __name__ == '__main__':
    main()

