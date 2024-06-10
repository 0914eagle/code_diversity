
def xor_sequence(seq):
    xor = 0
    for i in range(len(seq)):
        xor ^= seq[i]
    return xor

def count_pairs(seq):
    count = 0
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if xor_sequence(seq[i:j+1]) == sum(seq[i:j+1]):
                count += 1
    return count

def main():
    n = int(input())
    seq = list(map(int, input().split()))
    print(count_pairs(seq))

if __name__ == '__main__':
    main()

