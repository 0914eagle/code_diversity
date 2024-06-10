
def is_distinct(sequence):
    return len(set(sequence)) == len(sequence)

def solve():
    n = int(input())
    sequence = list(map(int, input().split()))
    if is_distinct(sequence):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()

