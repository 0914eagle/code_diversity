
def get_max_sum(numbers):
    # Calculate the sum of the given numbers
    sum = 0
    for num in numbers:
        sum += num
    
    # If the sum is already positive, return it
    if sum > 0:
        return sum
    
    # If the sum is negative, find the maximum sum by changing the signs of the numbers
    max_sum = 0
    for i in range(len(numbers)):
        # Calculate the sum of the numbers with the ith number and (i+1)th number changed
        sum1 = 0
        sum2 = 0
        for j in range(len(numbers)):
            if j == i or j == i+1:
                sum1 += numbers[j]
            else:
                sum2 += numbers[j]
        max_sum = max(max_sum, abs(sum1), abs(sum2))
    return max_sum

def main():
    numbers = list(map(int, input().split()))
    print(get_max_sum(numbers))

if __name__ == '__main__':
    main()

