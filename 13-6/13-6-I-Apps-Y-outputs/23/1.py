
def find_largest(numbers):
    return max(numbers)

def find_smallest(numbers):
    return min(numbers)

def find_sum(numbers):
    return sum(numbers)

def find_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def find_average(numbers):
    return sum(numbers) / len(numbers)

def find_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1]) / 2
    else:
        return numbers[len(numbers)//2]

def find_mode(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    return [key for key, value in counts.items() if value == max_count]

def find_range(numbers):
    return max(numbers) - min(numbers)

def find_variance(numbers):
    mean = find_average(numbers)
    return sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)

def find_standard_deviation(numbers):
    variance = find_variance(numbers)
    return variance ** 0.5

def find_confidence_interval(numbers, confidence=0.95):
    mean = find_average(numbers)
    standard_deviation = find_standard_deviation(numbers)
    t_value = t.ppf((1 + confidence) / 2, len(numbers) - 1)
    half_width = t_value * standard_deviation / sqrt(len(numbers))
    return (mean - half_width, mean + half_width)

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(find_largest(numbers))
    print(find_smallest(numbers))
    print(find_sum(numbers))
    print(find_product(numbers))
    print(find_average(numbers))
    print(find_median(numbers))
    print(find_mode(numbers))
    print(find_range(numbers))
    print(find_variance(numbers))
    print(find_standard_deviation(numbers))
    print(find_confidence_interval(numbers))

