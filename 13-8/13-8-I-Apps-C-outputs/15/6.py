
import itertools

def is_sorted(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                return False
    return True

def count_unsorted_sequences(seq):
    count = 0
    for perm in itertools.permutations(seq):
        if not is_sorted(perm):
            count += 1
    return count % (10**9 + 9)

def main():
    n = int(input())
    seq = tuple(int(x) for x in input().split())
    print(count_unsorted_sequences(seq))

if __name__ == '__main__':
    main()

