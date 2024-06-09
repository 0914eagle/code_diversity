
def read_input():
    N = int(input())
    P = []
    for i in range(N):
        P.append(int(input()))
    return N, P

def calculate_x(N, P):
    x = 0
    for i in range(N):
        x += P[i]
    return x

def main():
    N, P = read_input()
    x = calculate_x(N, P)
    print(x)

if __name__ == '__main__':
    main()

