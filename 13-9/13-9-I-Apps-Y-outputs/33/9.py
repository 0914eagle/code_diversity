
def read_input():
    N = int(input())
    H = list(map(int, input().split()))
    return N, H

def get_maximum_moves(H):
    max_moves = 0
    for i in range(len(H)):
        if i > 0 and H[i] >= H[i-1]:
            max_moves += 1
    return max_moves

def main():
    N, H = read_input()
    print(get_maximum_moves(H))

if __name__ == '__main__':
    main()

