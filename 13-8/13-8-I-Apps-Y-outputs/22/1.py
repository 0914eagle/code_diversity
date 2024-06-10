
def get_input():
    return list(map(int, input().split()))

def solve(N, A):
    sheet = set()
    for i in range(N):
        if A[i] in sheet:
            sheet.remove(A[i])
        else:
            sheet.add(A[i])
    return len(sheet)

def main():
    N = get_input()[0]
    A = get_input()[1:]
    print(solve(N, A))

if __name__ == '__main__':
    main()

