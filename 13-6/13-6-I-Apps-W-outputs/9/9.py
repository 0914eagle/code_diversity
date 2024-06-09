
def get_max_sum(numbers):
    # Calculate the sum of the given numbers
    sum = 0
    for num in numbers:
        sum += num
    # Return the sum
    return sum

def get_max_sum_after_operations(numbers):
    # Calculate the sum of the given numbers
    sum = 0
    for num in numbers:
        sum += num
    # Return the sum
    return sum

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(int(input()))]
    print(get_max_sum(numbers))
    print(get_max_sum_after_operations(numbers))

