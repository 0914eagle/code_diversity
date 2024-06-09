
def f1(n, numbers):
    # find the number of odd numbers in the list
    odd_numbers = 0
    for num in numbers:
        if num % 2 == 1:
            odd_numbers += 1
    
    # find the number of ways Ivana can make the first move
    first_moves = 0
    for i in range(n):
        if numbers[i] % 2 == 1:
            first_moves += 1
    
    return first_moves

def f2(n, numbers):
    # find the number of ways Ivana can make the first move and win
    first_moves = 0
    for i in range(n):
        if numbers[i] % 2 == 1:
            first_moves += 1
    
    return first_moves

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(f2(n, numbers))

