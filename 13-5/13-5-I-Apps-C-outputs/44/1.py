
def get_good_sequences(good_integers):
    good_sequences = []
    for i in range(len(good_integers)):
        sequence = [good_integers[i]]
        for j in range(i+1, len(good_integers)):
            if good_integers[j] > sequence[-1] and gcd(sequence[-1], good_integers[j]) == 1:
                sequence.append(good_integers[j])
        if len(sequence) > 1:
            good_sequences.append(sequence)
    return good_sequences

def get_longest_sequence(good_sequences):
    return max(good_sequences, key=len)

def main():
    n = int(input())
    good_integers = [int(x) for x in input().split()]
    good_sequences = get_good_sequences(good_integers)
    longest_sequence = get_longest_sequence(good_sequences)
    print(len(longest_sequence))

if __name__ == '__main__':
    main()

