
def find_largest_number(numbers):
    return max(numbers)

def find_smallest_number(numbers):
    return min(numbers)

def find_sum_of_numbers(numbers):
    return sum(numbers)

def find_product_of_numbers(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def find_average_of_numbers(numbers):
    return sum(numbers) / len(numbers)

def find_median_of_numbers(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]

def find_mode_of_numbers(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    max_count = max(counts.values())
    return [number for number, count in counts.items() if count == max_count]

def find_range_of_numbers(numbers):
    return max(numbers) - min(numbers)

def find_variance_of_numbers(numbers):
    mean = find_average_of_numbers(numbers)
    return sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)

def find_standard_deviation_of_numbers(numbers):
    return variance ** 0.5

def find_confidence_interval_of_numbers(numbers, confidence=0.95):
    mean = find_average_of_numbers(numbers)
    standard_deviation = find_standard_deviation_of_numbers(numbers)
    t_value = t.ppf(confidence, len(numbers) - 1)
    margin_of_error = t_value * standard_deviation / sqrt(len(numbers))
    return (mean - margin_of_error, mean + margin_of_error)

def find_correlation_coefficient_of_numbers(numbers1, numbers2):
    mean1 = find_average_of_numbers(numbers1)
    mean2 = find_average_of_numbers(numbers2)
    sum_of_products = sum((x1 - mean1) * (x2 - mean2) for x1, x2 in zip(numbers1, numbers2))
    sum_of_squares1 = sum((x - mean1) ** 2 for x in numbers1)
    sum_of_squares2 = sum((x - mean2) ** 2 for x in numbers2)
    return sum_of_products / (sqrt(sum_of_squares1) * sqrt(sum_of_squares2))

if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    print(find_largest_number(numbers))
    print(find_smallest_number(numbers))
    print(find_sum_of_numbers(numbers))
    print(find_product_of_numbers(numbers))
    print(find_average_of_numbers(numbers))
    print(find_median_of_numbers(numbers))
    print(find_mode_of_numbers(numbers))
    print(find_range_of_numbers(numbers))
    print(find_variance_of_numbers(numbers))
    print(find_standard_deviation_of_numbers(numbers))
    print(find_confidence_interval_of_numbers(numbers))
    print(find_correlation_coefficient_of_numbers(numbers, 0.95))

