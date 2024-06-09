
def get_min_d(a):
    # Calculate the sum of the elements in the array
    sum_a = sum(a)
    
    # Calculate the minimum value of D that can be used to make all elements equal
    min_d = sum_a // len(a)
    
    # Check if min_d is a valid value of D
    if min_d * len(a) == sum_a:
        return min_d
    else:
        return -1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min_d(a))

if __name__ == '__main__':
    main()

