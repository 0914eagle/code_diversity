
def get_blue_balls(n, a, b):
    blue_balls = 0
    for i in range(n):
        if i % (a + b) < a:
            blue_balls += 1
    return blue_balls

def main():
    n, a, b = map(int, input().split())
    print(get_blue_balls(n, a, b))

if __name__ == '__main__':
    main()

