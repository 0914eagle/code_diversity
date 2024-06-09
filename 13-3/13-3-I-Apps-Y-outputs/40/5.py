
def get_max_value(sequence, index):
    return max(sequence[:index] + sequence[index+1:])

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    for i in range(n):
        print(get_max_value(sequence, i))

