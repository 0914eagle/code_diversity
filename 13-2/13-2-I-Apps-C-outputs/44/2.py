
def f1(n, numbers):
    # find the numbers that are adjacent to the first number
    adjacent_numbers = []
    for i in range(n):
        if numbers[i] in [numbers[(i-1)%n], numbers[(i+1)%n]]:
            adjacent_numbers.append(numbers[i])
    
    # find the numbers that are adjacent to the second number
    adjacent_numbers_2 = []
    for i in range(n):
        if numbers[(i-1)%n] in [numbers[i], numbers[(i+1)%n]]:
            adjacent_numbers_2.append(numbers[i])
    
    # return the number of adjacent numbers that are not in the second list
    return len(set(adjacent_numbers) - set(adjacent_numbers_2))

def f2(n, numbers):
    # find the numbers that are adjacent to the first number
    adjacent_numbers = []
    for i in range(n):
        if numbers[i] in [numbers[(i-1)%n], numbers[(i+1)%n]]:
            adjacent_numbers.append(numbers[i])
    
    # find the numbers that are adjacent to the second number
    adjacent_numbers_2 = []
    for i in range(n):
        if numbers[(i-1)%n] in [numbers[i], numbers[(i+1)%n]]:
            adjacent_numbers_2.append(numbers[i])
    
    # return the number of adjacent numbers that are not in the second list
    return len(set(adjacent_numbers) - set(adjacent_numbers_2))

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(f1(n, numbers))
    print(f2(n, numbers))

