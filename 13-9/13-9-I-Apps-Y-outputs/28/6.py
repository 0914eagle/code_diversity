
def get_permutation(n):
    permutation = list(map(int, input().split()))
    return permutation

def get_second_smallest(permutation):
    count = 0
    for i in range(1, len(permutation) - 1):
        if permutation[i] < permutation[i - 1] and permutation[i] < permutation[i + 1]:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    permutation = get_permutation(n)
    print(get_second_smallest(permutation))

