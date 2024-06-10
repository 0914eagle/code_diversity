
def are_pairwise_distinct(sequence):
    return len(set(sequence)) == len(sequence)

def main():
    num_elements = int(input())
    sequence = list(map(int, input().split()))
    if are_pairwise_distinct(sequence):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

