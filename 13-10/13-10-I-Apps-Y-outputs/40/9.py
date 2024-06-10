
def get_unique_elements(my_list):
    unique_elements = []
    for element in my_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

def remove_duplicates(my_list):
    unique_elements = get_unique_elements(my_list)
    unique_elements.sort(reverse=True)
    for element in unique_elements:
        my_list.remove(element)
    return my_list

def main():
    my_list = [1, 5, 5, 1, 6, 1]
    print(remove_duplicates(my_list))

if __name__ == '__main__':
    main()

