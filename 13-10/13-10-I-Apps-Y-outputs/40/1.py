
def remove_duplicates(arr):
    unique_elements = set()
    unique_arr = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.add(element)
            unique_arr.append(element)
    return unique_arr

def print_array(arr):
    print(len(arr))
    for element in arr:
        print(element, end=" ")

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    unique_arr = remove_duplicates(arr)
    print_array(unique_arr)

if __name__ == '__main__':
    main()

