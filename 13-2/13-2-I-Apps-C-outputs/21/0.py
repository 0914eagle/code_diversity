
def f1(n, a):
    # Find the index of the smallest element in the list
    smallest_index = a.index(min(a))
    # Find the index of the largest element in the list
    largest_index = a.index(max(a))
    # If the smallest element is not at the start of the list, swap it with the first element
    if smallest_index != 0:
        a[smallest_index], a[0] = a[0], a[smallest_index]
    # If the largest element is not at the end of the list, swap it with the last element
    if largest_index != n-1:
        a[largest_index], a[n-1] = a[n-1], a[largest_index]
    return a

def f2(n, a):
    # Find the index of the smallest element in the list
    smallest_index = a.index(min(a))
    # Find the index of the largest element in the list
    largest_index = a.index(max(a))
    # If the smallest element is not at the start of the list, swap it with the first element
    if smallest_index != 0:
        a[smallest_index], a[0] = a[0], a[smallest_index]
    # If the largest element is not at the end of the list, swap it with the last element
    if largest_index != n-1:
        a[largest_index], a[n-1] = a[n-1], a[largest_index]
    return a

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

