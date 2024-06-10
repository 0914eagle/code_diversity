
def get_unique_elements(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

def get_rightmost_occurrences(arr):
    unique_elements = get_unique_elements(arr)
    rightmost_occurrences = []
    for element in unique_elements:
        rightmost_occurrences.append(element)
    return rightmost_occurrences

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    unique_elements = get_rightmost_occurrences(arr)
    print(len(unique_elements))
    print(*unique_elements)

if __name__ == '__main__':
    main()

