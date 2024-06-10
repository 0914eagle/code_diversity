
def get_max_odd_subsequence(numbers):
    max_sum = 0
    current_sum = 0
    for i in range(len(numbers)):
        current_sum += numbers[i]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum

def get_best_subsequence(numbers):
    max_sum = 0
    current_sum = 0
    for i in range(len(numbers)):
        current_sum += numbers[i]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_best_subsequence(numbers))

