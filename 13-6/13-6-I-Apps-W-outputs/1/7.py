
def get_coconut_picking_time(N, A, B):
    return (N * A) + (N * (N - 1) / 2) * B

def get_coconut_opening_time(M, C, D):
    return (M * C) + (M * (M - 1) / 2) * D

def get_time_difference(total_time, coconut_picking_time, coconut_opening_time):
    return total_time - coconut_picking_time - coconut_opening_time

def main():
    total_time = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    M = int(input())
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    coconut_picking_time = get_coconut_picking_time(N, A, B)
    coconut_opening_time = get_coconut_opening_time(M, C, D)
    time_difference = get_time_difference(total_time, coconut_picking_time, coconut_opening_time)

    print(time_difference)

if __name__ == '__main__':
    main()

