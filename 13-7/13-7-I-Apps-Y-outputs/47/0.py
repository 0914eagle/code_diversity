
def blue_balls_count(N, A, B):
    count = 0
    for i in range(N):
        if i % (A + B) < A:
            count += 1
    return count

def main():
    N, A, B = map(int, input().split())
    print(blue_balls_count(N, A, B))

if __name__ == '__main__':
    main()

