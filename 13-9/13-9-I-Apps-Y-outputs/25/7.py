
def get_input():
    return [list(map(int, input().split())) for _ in range(3)]

def is_correct(c):
    a_sum = sum(c[0])
    b_sum = sum(c[1])
    for i in range(3):
        for j in range(3):
            if c[i][j] != a_sum + b_sum:
                return False
    return True

def main():
    c = get_input()
    print("Yes") if is_correct(c) else print("No")

if __name__ == '__main__':
    main()

