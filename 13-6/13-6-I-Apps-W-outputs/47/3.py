
def find_subset(a):
    # find the sum of all elements in the array
    sum_a = sum(a)
    # check if the sum is even
    if sum_a % 2 == 0:
        # return the number of elements and their indexes
        return len(a), [i for i in range(1, len(a) + 1)]
    else:
        # return -1 if there is no such subset
        return -1

def main():
    # read the number of test cases
    t = int(input())
    # loop through the test cases
    for _ in range(t):
        # read the length of the array
        n = int(input())
        # read the array
        a = list(map(int, input().split()))
        # find the subset
        result = find_subset(a)
        # print the result
        if result == -1:
            print(-1)
        else:
            print(result[0])
            print(" ".join(map(str, result[1])))

if __name__ == '__main__':
    main()

