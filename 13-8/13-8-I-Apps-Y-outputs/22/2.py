
def solve(N, A):
    sheet = set()
    for i in range(N):
        if A[i] in sheet:
            sheet.remove(A[i])
        else:
            sheet.add(A[i])
    return len(sheet)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

if __name__ == '__main__':
    main()

