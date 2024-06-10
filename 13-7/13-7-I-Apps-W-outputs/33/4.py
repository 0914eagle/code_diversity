
def get_smallest_k(doors, sequence):
    k = 0
    left_doors = 0
    right_doors = 0
    for i in range(len(sequence)):
        if sequence[i] == 0:
            left_doors += 1
        else:
            right_doors += 1
        if left_doors > 0 and right_doors > 0:
            return k
        k += 1
    return k

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(get_smallest_k(n, sequence))

if __name__ == '__main__':
    main()

