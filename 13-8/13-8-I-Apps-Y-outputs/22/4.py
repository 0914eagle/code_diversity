
def game(N, A):
    sheet = set()
    for i in range(N):
        if A[i] in sheet:
            sheet.remove(A[i])
        else:
            sheet.add(A[i])
    return len(sheet)

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(game(N, A))

if __name__ == '__main__':
    main()

