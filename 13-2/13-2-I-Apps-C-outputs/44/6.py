
def f1(n, numbers):
    # find the number of odd numbers
    odd_numbers = 0
    for num in numbers:
        if num % 2 == 1:
            odd_numbers += 1
    
    # find the number of ways to choose two odd numbers
    ways = 0
    for i in range(odd_numbers):
        for j in range(i+1, odd_numbers):
            ways += 1
    
    return ways

def f2(n, numbers):
    # find the number of ways to choose two odd numbers
    ways = f1(n, numbers)
    
    # find the number of ways to choose two even numbers
    even_numbers = n - odd_numbers
    for i in range(even_numbers):
        for j in range(i+1, even_numbers):
            ways += 1
    
    return ways

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(f2(n, numbers))

