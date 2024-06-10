
def get_max_odd_subsequence(numbers):
    # find the maximum subsequence sum
    max_sum = max(sum(numbers[i:j]) for i in range(len(numbers)) for j in range(i + 1, len(numbers) + 1))
    
    # find all subsequence sums
    subsequence_sums = [sum(numbers[i:j]) for i in range(len(numbers)) for j in range(i + 1, len(numbers) + 1)]
    
    # find the subsequence sum that is odd and has the maximum value
    max_odd_sum = max([sum for sum in subsequence_sums if sum % 2 == 1], default=0)
    
    return max_odd_sum

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(get_max_odd_subsequence(numbers))

if __name__ == '__main__':
    main()

