
def remove_duplicates(arr):
    unique_elements = set()
    unique_arr = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.add(element)
            unique_arr.append(element)
    return unique_arr

def print_result(arr):
    print(len(arr))
    print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = remove_duplicates(arr)
    print_result(result)

