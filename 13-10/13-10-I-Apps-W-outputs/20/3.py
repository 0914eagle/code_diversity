
def max_odd_subsequence(numbers):
    # find the maximum subsequence sum
    max_sum = 0
    current_sum = 0
    for num in numbers:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    
    # find all subsequence sums
    subsequence_sums = []
    for i in range(len(numbers)):
        current_sum = 0
        for j in range(i, len(numbers)):
            current_sum += numbers[j]
            subsequence_sums.append(current_sum)
    
    # find the maximum odd subsequence sum
    max_odd_sum = 0
    for sum in subsequence_sums:
        if sum % 2 == 1 and sum > max_odd_sum:
            max_odd_sum = sum
    
    return max_odd_sum

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(max_odd_subsequence(numbers))

if __name__ == '__main__':
    main()

