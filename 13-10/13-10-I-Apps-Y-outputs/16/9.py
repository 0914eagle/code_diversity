
def get_good_array(a):
    n = len(a)
    if n % 6 == 0:
        return a
    
    # Find the minimum number of elements to remove to make the array good
    min_removals = n // 6
    for i in range(min_removals):
        if a[i] != 4 or a[i+1] != 8 or a[i+2] != 15 or a[i+3] != 16 or a[i+4] != 23 or a[i+5] != 42:
            min_removals += 1
    
    return a[:-min_removals]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(get_good_array(a)))

if __name__ == '__main__':
    main()

