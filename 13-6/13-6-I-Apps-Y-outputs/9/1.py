
def read_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return n, arr


def sort_array(arr):
    return sorted(arr)


def main():
    n, arr = read_input()
    sorted_arr = sort_array(arr)
    print(*sorted_arr, sep=' ')


if __name__ == '__main__':
    main()

