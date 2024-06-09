
def find_subset(a):
    # find the sum of all elements in the array
    sum_a = sum(a)
    # check if the sum is even
    if sum_a % 2 == 0:
        # return the number of elements in the array
        return len(a)
    else:
        # initialize a variable to keep track of the minimum number of elements needed to have an even sum
        min_elements = float('inf')
        # initialize a variable to keep track of the minimum sum
        min_sum = float('inf')
        # loop through all possible subsets of the array
        for i in range(1, len(a)+1):
            # get the combination of elements in the current subset
            combination = combinations(a, i)
            # loop through all combinations of elements in the current subset
            for comb in combination:
                # calculate the sum of the current combination
                sum_comb = sum(comb)
                # check if the sum is even
                if sum_comb % 2 == 0:
                    # calculate the number of elements in the current combination
                    num_elements = len(comb)
                    # check if the current combination has fewer elements than the minimum number of elements needed to have an even sum
                    if num_elements < min_elements:
                        # update the minimum number of elements needed to have an even sum
                        min_elements = num_elements
                        # update the minimum sum
                        min_sum = sum_comb
        # check if there is no subset with an even sum
        if min_elements == float('inf'):
            # return -1 if there is no subset with an even sum
            return -1
        else:
            # return the minimum number of elements needed to have an even sum
            return min_elements

def main():
    # read the number of test cases
    t = int(input())
    # loop through all test cases
    for _ in range(t):
        # read the length of the array
        n = int(input())
        # read the array
        a = list(map(int, input().split()))
        # find the subset of elements with an even sum
        result = find_subset(a)
        # check if there is no subset with an even sum
        if result == -1:
            # print -1
            print(-1)
        else:
            # print the number of elements in the subset
            print(result)
            # print the indexes of the elements in the subset
            print(*[i+1 for i in range(result)])

if __name__ == '__main__':
    main()

