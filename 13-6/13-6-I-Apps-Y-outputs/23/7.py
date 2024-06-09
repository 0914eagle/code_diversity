
def get_largest_element(my_list):
    return max(my_list)

def get_index_of_largest_element(my_list):
    return my_list.index(max(my_list))

if __name__ == '__main__':
    n = int(input())
    my_list = list(map(int, input().split()))
    largest_element = get_largest_element(my_list)
    index_of_largest_element = get_index_of_largest_element(my_list)
    print(index_of_largest_element)

