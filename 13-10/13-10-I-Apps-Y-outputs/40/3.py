
def remove_duplicates(arr):
    unique_elements = set()
    unique_arr = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.add(element)
            unique_arr.append(element)
    return unique_arr

def print_unique_elements(arr):
    unique_elements = set()
    for element in arr:
        if element not in unique_elements:
            print(element, end=" ")
            unique_elements.add(element)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    unique_arr = remove_duplicates(arr)
    print(len(unique_arr))
    print_unique_elements(unique_arr)

