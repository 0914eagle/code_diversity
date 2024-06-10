
def remove_duplicates(arr):
    unique_elements = set()
    unique_arr = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.add(element)
            unique_arr.append(element)
    return unique_arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    unique_arr = remove_duplicates(arr)
    print(len(unique_arr))
    print(" ".join(map(str, unique_arr)))

if __name__ == '__main__':
    main()

