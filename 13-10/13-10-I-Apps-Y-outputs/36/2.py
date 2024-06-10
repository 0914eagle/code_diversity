
def get_base_2_representation(N):
    if N == 0:
        return "0"
    base_2_representation = ""
    while N != 0:
        if N % 2 == 0:
            base_2_representation = "0" + base_2_representation
        else:
            base_2_representation = "1" + base_2_representation
        N = N // 2
    return base_2_representation

def solve():
    N = int(input())
    base_2_representation = get_base_2_representation(N)
    print(base_2_representation)

if __name__ == '__main__':
    solve()

