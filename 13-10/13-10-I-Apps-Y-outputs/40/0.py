
def get_unique_elements(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

def remove_duplicates(arr):
    unique_elements = get_unique_elements(arr)
    rightmost_occurrences = []
    for element in unique_elements:
        rightmost_occurrences.append(arr[arr.index(element)])
    return rightmost_occurrences

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = remove_duplicates(arr)
    print(len(result))
    print(*result)

