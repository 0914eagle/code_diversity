
def solve(H, A):
    return (H-1) // A + 1

def main():
    H, A = map(int, input().split())
    print(solve(H, A))

if __name__ == '__main__':
    main()

