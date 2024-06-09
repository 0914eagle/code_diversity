
def get_unique_elements(my_list):
    return list(set(my_list))

def get_largest_element(my_list):
    return max(my_list)

def get_elements_greater_than_largest(my_list):
    largest = get_largest_element(my_list)
    return [x for x in my_list if x > largest]

def get_elements_less_than_largest(my_list):
    largest = get_largest_element(my_list)
    return [x for x in my_list if x < largest]

def get_unique_elements_greater_than_largest(my_list):
    return get_unique_elements(get_elements_greater_than_largest(my_list))

def get_unique_elements_less_than_largest(my_list):
    return get_unique_elements(get_elements_less_than_largest(my_list))

def get_answer(my_list):
    unique_greater = get_unique_elements_greater_than_largest(my_list)
    unique_less = get_unique_elements_less_than_largest(my_list)
    if len(unique_greater) == 0 and len(unique_less) == 0:
        return 0
    elif len(unique_greater) == 0 and len(unique_less) == 1:
        return 1
    elif len(unique_greater) == 1 and len(unique_less) == 0:
        return 2
    else:
        return 3

if __name__ == '__main__':
    n = int(input())
    my_list = list(map(int, input().split()))
    print(get_answer(my_list))

