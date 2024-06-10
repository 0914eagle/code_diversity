
def get_input():
    return list(map(int, input().split()))

def solve(x, y):
    for i in range(1, x+1):
        for j in range(1, x+1):
            if i + j == x and i * 2 + j * 4 == y:
                return "Yes"
    return "No"

if __name__ == '__main__':
    x, y = get_input()
    print(solve(x, y))

