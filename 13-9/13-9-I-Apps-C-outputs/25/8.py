
def input_array(n, m):
    array = []
    for i in range(n):
        array.append(int(input()))
    return array

def lossy_sort(array):
    # Your code here
    pass

def main():
    n, m = map(int, input().split())
    array = input_array(n, m)
    sorted_array = lossy_sort(array)
    print(*sorted_array, sep='\n')

if __name__ == '__main__':
    main()

