
def input_sequence():
    n = int(input())
    sequence = list(map(int, input().split()))
    return n, sequence

def are_distinct(sequence):
    return len(set(sequence)) == len(sequence)

def solve():
    n, sequence = input_sequence()
    if are_distinct(sequence):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
