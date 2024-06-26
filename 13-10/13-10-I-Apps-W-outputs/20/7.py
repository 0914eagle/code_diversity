
def get_odd_subsequence(numbers):
    # Initialize variables
    max_sum = 0
    current_sum = 0
    start_index = 0
    end_index = 0
    
    # Iterate through the array
    for i in range(len(numbers)):
        current_sum += numbers[i]
        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i
        if current_sum < 0:
            current_sum = 0
            start_index = i + 1
    
    # Return the subsequence
    return numbers[start_index:end_index+1]

def get_subsequence_sum(subsequence):
    return sum(subsequence)

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    subsequence = get_odd_subsequence(numbers)
    print(get_subsequence_sum(subsequence))

