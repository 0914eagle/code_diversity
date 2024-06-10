
def get_input():
    N = int(input())
    A = [int(i) for i in input().split()]
    return N, A

def solve(N, A):
    sheet = set()
    for a in A:
        if a in sheet:
            sheet.remove(a)
        else:
            sheet.add(a)
    return len(sheet)

def main():
    N, A = get_input()
    print(solve(N, A))

if __name__ == '__main__':
    main()

