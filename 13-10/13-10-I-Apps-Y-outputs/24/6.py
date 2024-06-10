
def get_available_megabytes(X, N, P):
    available_megabytes = X
    for i in range(N):
        available_megabytes += P[i]
        if available_megabytes > X:
            available_megabytes = available_megabytes % X
    return available_megabytes

def main():
    X = int(input())
    N = int(input())
    P = []
    for i in range(N):
        P.append(int(input()))
    available_megabytes = get_available_megabytes(X, N, P)
    print(available_megabytes)

if __name__ == '__main__':
    main()

