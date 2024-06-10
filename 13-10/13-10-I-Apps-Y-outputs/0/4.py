
def is_pairwise_distinct(sequence):
    return len(set(sequence)) == len(sequence)

def main():
    N = int(input())
    sequence = list(map(int, input().split()))
    if is_pairwise_distinct(sequence):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

