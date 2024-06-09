
def is_good_sequence(sequence):
    if len(sequence) < 2:
        return False
    if sequence[0] != 1:
        return False
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i-1] or sequence[i] - sequence[i-1] != 1:
            return False
    return True

def longest_good_sequence(good_integers):
    max_length = 0
    for i in range(len(good_integers)):
        for j in range(i+1, len(good_integers)):
            sequence = good_integers[i:j+1]
            if is_good_sequence(sequence):
                max_length = max(max_length, len(sequence))
    return max_length

if __name__ == '__main__':
    n = int(input())
    good_integers = list(map(int, input().split()))
    print(longest_good_sequence(good_integers))

