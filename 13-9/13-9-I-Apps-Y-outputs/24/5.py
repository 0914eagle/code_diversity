
def get_maximum_absolute_difference(sequence):
    maximum_difference = 0
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            difference = abs(sequence[i] - sequence[j])
            if difference > maximum_difference:
                maximum_difference = difference
    return maximum_difference

def main():
    sequence = list(map(int, input().split()))
    print(get_maximum_absolute_difference(sequence))

if __name__ == '__main__':
    main()

