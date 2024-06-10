
def get_max_odd_subsequence(numbers):
    # find the maximum subsequence sum
    max_sum = max(sum(numbers[i:j] for i in range(len(numbers)) for j in range(i+1, len(numbers)+1))
    
    # find all subsequences with odd sum
    odd_subsequences = [sum(numbers[i:j]) for i in range(len(numbers)) for j in range(i+1, len(numbers)+1) if sum(numbers[i:j]) % 2 == 1]
    
    # return the maximum odd subsequence sum
    return max(odd_subsequences)

def main():
    numbers = [int(input()) for _ in range(int(input()))]
    print(get_max_odd_subsequence(numbers))

if __name__ == '__main__':
    main()

