
def count_second_smallest(permutation):
    n = len(permutation)
    count = 0
    for i in range(1, n-1):
        if permutation[i] < permutation[i-1] and permutation[i] < permutation[i+1]:
            count += 1
    return count

def main():
    n = int(input())
    permutation = list(map(int, input().split()))
    print(count_second_smallest(permutation))

if __name__ == '__main__':
    main()

