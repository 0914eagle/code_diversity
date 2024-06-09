
def get_max_xor_sum(numbers):
    max_sum = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] ^ numbers[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum

