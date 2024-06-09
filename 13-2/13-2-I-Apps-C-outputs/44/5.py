
def f1(n, numbers):
    # find the number of odd numbers
    odd_numbers = 0
    for num in numbers:
        if num % 2 == 1:
            odd_numbers += 1
    
    # find the number of ways to choose the first number
    ways = 0
    for i in range(n):
        if numbers[i] % 2 == 1:
            ways += 1
    
    return ways

def f2(n, numbers):
    # find the number of ways to choose the first number
    ways = 0
    for i in range(n):
        if numbers[i] % 2 == 1:
            ways += 1
    
    return ways

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(f1(n, numbers))

