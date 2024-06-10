
def is_increasing(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

def fill_sequence(a, b):
    result = []
    for i in range(len(a)):
        if a[i] == 0:
            result.append(b.pop())
        else:
            result.append(a[i])
    return result

def solve(n, k, a, b):
    result = fill_sequence(a, b)
    return "Yes" if not is_increasing(result) else "No"

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, k, a, b))

