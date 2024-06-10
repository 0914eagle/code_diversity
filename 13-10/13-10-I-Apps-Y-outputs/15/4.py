
def get_value_from_powers(P1, P2):
    x = 0
    for i in range(len(P1)):
        x += P1[i] ** P2[i]
    return x

def get_value_from_sum(P1, P2):
    return sum(P1)

if __name__ == '__main__':
    N = int(input())
    P1 = []
    P2 = []
    for i in range(N):
        P1.append(int(input()))
        P2.append(int(input()))
    print(get_value_from_powers(P1, P2))

