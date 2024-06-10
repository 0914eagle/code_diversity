
def get_input():
    N = int(input())
    A = [int(i) for i in input().split()]
    return N, A

def solve(N, A):
    sheet = set()
    for i in range(N):
        if A[i] in sheet:
            sheet.remove(A[i])
        else:
            sheet.add(A[i])
    return len(sheet)

def main():
    N, A = get_input()
    print(solve(N, A))

if __name__ == '__main__':
    main()

