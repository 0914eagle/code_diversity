
def find_min_moves(a):
    n = len(a)
    # Initialize the minimum number of moves to be the number of books
    min_moves = n
    # Loop through each position on the bookshelf
    for i in range(n):
        # If there is a book at the current position
        if a[i] == 1:
            # Find the leftmost and rightmost positions of the contiguous segment starting from the current position
            left = i
            right = i
            while left >= 1 and a[left - 1] == 1:
                left -= 1
            while right < n and a[right + 1] == 1:
                right += 1
            # Calculate the number of moves required to shift the segment to the right
            moves_right = right - left + 1
            # Calculate the number of moves required to shift the segment to the left
            moves_left = left - i + 1
            # Update the minimum number of moves if necessary
            min_moves = min(min_moves, moves_right, moves_left)
    return min_moves

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(find_min_moves(a))

if __name__ == '__main__':
    main()

