
def get_maximum_absolute_difference(sequence):
    # find the maximum absolute difference of two elements (with different indices) in the sequence
    max_diff = 0
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            diff = abs(sequence[i] - sequence[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def main():
    # read the sequence from stdin
    sequence = list(map(int, input().split()))
    # find the maximum absolute difference of two elements (with different indices) in the sequence
    max_diff = get_maximum_absolute_difference(sequence)
    # print the result
    print(max_diff)

if __name__ == '__main__':
    main()

