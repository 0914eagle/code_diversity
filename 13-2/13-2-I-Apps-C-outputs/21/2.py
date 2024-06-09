
def f1(n, a):
    # Find the index of the smallest element in the list
    smallest_index = a.index(min(a))
    # Find the index of the largest element in the list
    largest_index = a.index(max(a))
    # Check if the smallest element is not at the beginning of the list
    if smallest_index != 0:
        # Swap the smallest element with the element at index 0
        a[smallest_index], a[0] = a[0], a[smallest_index]
        return a
    # Check if the largest element is not at the end of the list
    if largest_index != n-1:
        # Swap the largest element with the element at index n-1
        a[largest_index], a[n-1] = a[n-1], a[largest_index]
        return a
    return "impossible"

def f2(n, a):
    # Find the index of the smallest element in the list
    smallest_index = a.index(min(a))
    # Find the index of the largest element in the list
    largest_index = a.index(max(a))
    # Check if the smallest element is not at the beginning of the list
    if smallest_index != 0:
        # Swap the smallest element with the element at index 0
        a[smallest_index], a[0] = a[0], a[smallest_index]
        return a
    # Check if the largest element is not at the end of the list
    if largest_index != n-1:
        # Swap the largest element with the element at index n-1
        a[largest_index], a[n-1] = a[n-1], a[largest_index]
        return a
    return "impossible"

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

