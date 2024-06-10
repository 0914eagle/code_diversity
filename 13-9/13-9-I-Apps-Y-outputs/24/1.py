
def get_max_diff(A):
    max_diff = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            diff = abs(A[i] - A[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(get_max_diff(A))

if __name__ == '__main__':
    main()

