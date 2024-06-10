
def get_blue_balls(N, A, B):
    blue_balls = 0
    for i in range(N):
        if i % (A + B) < A:
            blue_balls += 1
    return blue_balls

def main():
    N, A, B = map(int, input().split())
    print(get_blue_balls(N, A, B))

if __name__ == '__main__':
    main()

