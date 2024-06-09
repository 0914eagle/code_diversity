
def is_good_sequence(sequence):
    if len(sequence) < 2:
        return True
    if sequence[0] > sequence[1]:
        return False
    if sequence[0] % sequence[1] == 0:
        return False
    return is_good_sequence(sequence[1:])

def longest_good_sequence(numbers):
    max_length = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sequence = numbers[i:j+1]
            if is_good_sequence(sequence):
                max_length = max(max_length, len(sequence))
    return max_length

if __name__ == '__main__':
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(longest_good_sequence(numbers))

