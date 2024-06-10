
def read_input():
    return list(map(int, input().split()))

def is_confused(seq):
    return sum(seq[i] > seq[i+1] for i in range(len(seq)-1))

def count_sequences(N, C):
    return len([seq for seq in itertools.permutations(range(1, N+1)) if is_confused(seq) == C])

def main():
    N, C = read_input()
    print(count_sequences(N, C) % 1000000007)

if __name__ == '__main__':
    main()

