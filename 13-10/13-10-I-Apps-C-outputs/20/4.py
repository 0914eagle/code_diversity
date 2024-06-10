
def solve(A, B):
    # Calculate the number of appearances of numbers from the interval [A, B]
    count = 0
    for i in range(A, B+1):
        count += 1
    return count

def main():
    Q = int(input())
    for i in range(Q):
        A, B = map(int, input().split())
        print(solve(A, B))

if __name__ == '__main__':
    main()

