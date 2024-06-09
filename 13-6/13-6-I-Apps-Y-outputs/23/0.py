
def get_largest_element(my_list):
    return max(my_list)

def get_smallest_element(my_list):
    return min(my_list)

def get_sum_of_elements(my_list):
    return sum(my_list)

def get_product_of_elements(my_list):
    result = 1
    for element in my_list:
        result *= element
    return result

def get_mean_of_elements(my_list):
    return sum(my_list) / len(my_list)

def get_median_of_elements(my_list):
    sorted_list = sorted(my_list)
    if len(my_list) % 2 == 0:
        mid = len(my_list) // 2
        return (sorted_list[mid] + sorted_list[mid - 1]) / 2
    else:
        mid = len(my_list) // 2
        return sorted_list[mid]

def get_mode_of_elements(my_list):
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    max_count = max(counts.values())
    return [key for key, value in counts.items() if value == max_count]

def get_variance_of_elements(my_list):
    mean = get_mean_of_elements(my_list)
    return sum((x - mean) ** 2 for x in my_list) / (len(my_list) - 1)

def get_standard_deviation_of_elements(my_list):
    variance = get_variance_of_elements(my_list)
    return variance ** 0.5

if __name__ == '__main__':
    n = int(input())
    my_list = list(map(int, input().split()))
    print(get_largest_element(my_list))
    print(get_smallest_element(my_list))
    print(get_sum_of_elements(my_list))
    print(get_product_of_elements(my_list))
    print(get_mean_of_elements(my_list))
    print(get_median_of_elements(my_list))
    print(get_mode_of_elements(my_list))
    print(get_variance_of_elements(my_list))
    print(get_standard_deviation_of_elements(my_list))

