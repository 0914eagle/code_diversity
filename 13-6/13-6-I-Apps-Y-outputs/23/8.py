
def find_largest_element(my_list):
    return max(my_list)

def find_smallest_element(my_list):
    return min(my_list)

def find_second_largest_element(my_list):
    return sorted(my_list)[-2]

def find_second_smallest_element(my_list):
    return sorted(my_list)[1]

def find_sum_of_elements(my_list):
    return sum(my_list)

def find_product_of_elements(my_list):
    result = 1
    for element in my_list:
        result *= element
    return result

def find_average_of_elements(my_list):
    return sum(my_list) / len(my_list)

def find_median_of_elements(my_list):
    sorted_list = sorted(my_list)
    if len(my_list) % 2 == 0:
        return (sorted_list[len(my_list) // 2 - 1] + sorted_list[len(my_list) // 2]) / 2
    else:
        return sorted_list[len(my_list) // 2]

def find_mode_of_elements(my_list):
    counts = {}
    for element in my_list:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    max_count = max(counts.values())
    modes = [key for key, value in counts.items() if value == max_count]
    return modes[0]

if __name__ == '__main__':
    n = int(input())
    my_list = list(map(int, input().split()))
    print(find_largest_element(my_list))
    print(find_smallest_element(my_list))
    print(find_second_largest_element(my_list))
    print(find_second_smallest_element(my_list))
    print(find_sum_of_elements(my_list))
    print(find_product_of_elements(my_list))
    print(find_average_of_elements(my_list))
    print(find_median_of_elements(my_list))
    print(find_mode_of_elements(my_list))

