
def get_max_sum(numbers):
    # Calculate the sum of the given numbers
    sum = 0
    for num in numbers:
        sum += num
    # Return the sum
    return sum

def get_max_sum_with_operation(numbers):
    # Calculate the sum of the given numbers
    sum = 0
    for num in numbers:
        sum += num
    # Return the sum
    return sum

if __name__ == '__main__':
    num_list = list(map(int, input().split()))
    result = get_max_sum(num_list)
    print(result)

