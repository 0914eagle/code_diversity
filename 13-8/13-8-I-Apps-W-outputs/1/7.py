
def is_increasing_sequence(sequence):
    return all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))

def replace_zeros(a, b):
    result = []
    for i in range(len(a)):
        if a[i] == 0:
            result.append(b.pop())
        else:
            result.append(a[i])
    return result

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = replace_zeros(a, b)
    if is_increasing_sequence(result):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()

