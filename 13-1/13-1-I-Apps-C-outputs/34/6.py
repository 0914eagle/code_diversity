
def find_max_average(numbers, k):
    
    if len(numbers) < k:
        return -1
    
    max_sum = 0
    current_sum = 0
    for i in range(k):
        max_sum += numbers[i]
    
    for i in range(k, len(numbers)):
        current_sum += numbers[i]
        current_sum -= numbers[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum / k

