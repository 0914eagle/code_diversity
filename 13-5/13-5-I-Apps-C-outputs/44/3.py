
def is_good_sequence(sequence):
    if len(sequence) < 2:
        return True
    if sequence[0] > sequence[1]:
        return False
    if sequence[0] % sequence[1] == 0:
        return False
    return is_good_sequence(sequence[1:])

def find_longest_good_sequence(good_integers):
    longest_sequence = []
    for i in range(len(good_integers)):
        current_sequence = [good_integers[i]]
        for j in range(i+1, len(good_integers)):
            if good_integers[j] % good_integers[i] == 0:
                break
            current_sequence.append(good_integers[j])
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
    return longest_sequence

if __name__ == '__main__':
    n = int(input())
    good_integers = list(map(int, input().split()))
    print(len(find_longest_good_sequence(good_integers)))

