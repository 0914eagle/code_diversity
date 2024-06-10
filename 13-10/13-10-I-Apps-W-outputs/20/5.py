
def get_odd_subsequence(numbers):
    
    # initialize variables
    max_sum = 0
    current_sum = 0
    subsequence = []
    
    # iterate over the numbers
    for i in range(len(numbers)):
        # add the current number to the current subsequence
        subsequence.append(numbers[i])
        current_sum += numbers[i]
        
        # check if the current sum is odd and greater than the maximum sum
        if current_sum % 2 == 1 and current_sum > max_sum:
            max_sum = current_sum
        
        # check if the current sum is negative and remove the first element from the subsequence
        while current_sum < 0:
            current_sum -= subsequence.pop(0)
    
    return subsequence

def main():
    # read the input
    n = int(input())
    numbers = [int(x) for x in input().split()]
    
    # find the subsequence with the maximum odd sum
    subsequence = get_odd_subsequence(numbers)
    
    # print the sum of the subsequence
    print(sum(subsequence))

if __name__ == '__main__':
    main()

