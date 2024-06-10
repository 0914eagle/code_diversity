
def get_min_moves(a):
    # Find the starting position of the first book
    start = 0
    while a[start] == 0:
        start += 1
    
    # Initialize the minimum number of moves to 0
    min_moves = 0
    
    # Loop through the array and find the contiguous segments of books
    for i in range(start, len(a)):
        if a[i] == 1:
            # If we find a book, check if the previous book is also present
            if i > 0 and a[i-1] == 0:
                # If the previous book is not present, we need to move this book to the left
                min_moves += 1
            # Update the starting position of the next contiguous segment
            start = i
    
    return min_moves

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_min_moves(a))

if __name__ == '__main__':
    main()

