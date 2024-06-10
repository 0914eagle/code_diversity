
def read_input():
    n = int(input())
    numbers = list(map(int, input().split()))
    return n, numbers

def count_first_moves(n, numbers):
    # Initialize a set to store the first moves
    first_moves = set()
    
    # Iterate through the numbers and find the adjacent numbers
    for i in range(n):
        left = (i - 1) % n
        right = (i + 1) % n
        first_moves.add(numbers[left])
        first_moves.add(numbers[right])
    
    # Return the number of first moves
    return len(first_moves)

def main():
    n, numbers = read_input()
    print(count_first_moves(n, numbers))

if __name__ == '__main__':
    main()

