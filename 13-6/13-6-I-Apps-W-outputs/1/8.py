
def get_total_time(N, A, B):
    return sum(A) + sum(B)

def get_second_type_arrival_time(N, A, B, M, C, D):
    total_time = get_total_time(N, A, B)
    second_type_arrival_time = total_time - sum(C) - sum(D)
    return second_type_arrival_time

def main():
    total_time = int(input())
    N = int(input())
    A = []
    B = []
    for i in range(N):
        A.append(int(input()))
        B.append(int(input()))
    M = int(input())
    C = []
    D = []
    for i in range(M):
        C.append(int(input()))
        D.append(int(input()))
    print(get_second_type_arrival_time(N, A, B, M, C, D))

if __name__ == '__main__':
    main()

