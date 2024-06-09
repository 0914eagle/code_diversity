
def read_input():
    N = int(input())
    numbers = [int(i) for i in input().split()]
    return N, numbers

def f1(N, numbers):
    # find the number of odd numbers
    odd_count = 0
    for num in numbers:
        if num % 2 == 1:
            odd_count += 1
    
    # find the number of moves
    moves = 0
    for i in range(N):
        if i % 2 == 0:
            moves += 1
        else:
            moves += 2
    
    # find the number of first moves
    first_moves = 0
    for i in range(N):
        if i % 2 == 0:
            first_moves += 1
        else:
            first_moves += 2
    
    return first_moves

def f2(N, numbers):
    # find the number of odd numbers
    odd_count = 0
    for num in numbers:
        if num % 2 == 1:
            odd_count += 1
    
    # find the number of moves
    moves = 0
    for i in range(N):
        if i % 2 == 0:
            moves += 1
        else:
            moves += 2
    
    # find the number of first moves
    first_moves = 0
    for i in range(N):
        if i % 2 == 0:
            first_moves += 1
        else:
            first_moves += 2
    
    return first_moves

if __name__ == '__main__':
    N, numbers = read_input()
    print(f1(N, numbers))
    print(f2(N, numbers))

