
def get_best_subsequence(numbers):
    # Initialize variables
    max_sum = 0
    current_sum = 0
    subsequence = []
    
    # Iterate through the input sequence
    for i in range(len(numbers)):
        current_sum += numbers[i]
        subsequence.append(numbers[i])
        
        # If the current sum is odd and greater than the maximum sum, update the maximum sum and subsequence
        if current_sum % 2 != 0 and current_sum > max_sum:
            max_sum = current_sum
        
        # If the current sum is even, update the subsequence and reset the current sum
        if current_sum % 2 == 0:
            subsequence = subsequence[1:]
            current_sum = 0
    
    # Return the subsequence with the maximum sum
    return subsequence

def get_subsequence_sum(subsequence):
    return sum(subsequence)

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    subsequence = get_best_subsequence(numbers)
    print(get_subsequence_sum(subsequence))

