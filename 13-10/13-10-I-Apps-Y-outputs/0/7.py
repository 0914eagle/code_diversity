
def is_pairwise_distinct(arr):
    return len(set(arr)) == len(arr)

def input_sequence():
    n = int(input())
    arr = list(map(int, input().split()))
    return arr

if __name__ == '__main__':
    arr = input_sequence()
    if is_pairwise_distinct(arr):
        print("YES")
    else:
        print("NO")

