
def check_consistency(n, a, b, c, d):
    for i in range(n):
        x_i = random.randint(a - b, a + b)
        if x_i < c - d or x_i > c + d:
            return False
    return True

def main():
    t = int(input())
    for i in range(t):
        n, a, b, c, d = map(int, input().split())
        if check_consistency(n, a, b, c, d):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

