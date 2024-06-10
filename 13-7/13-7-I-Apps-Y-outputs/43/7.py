
def get_input():
    return list(map(int, input().split()))

def solve(L, R):
    min_value = float('inf')
    for i in range(L, R):
        for j in range(i+1, R+1):
            value = (i * j) % 2019
            if value < min_value:
                min_value = value
    return min_value

def main():
    L, R = get_input()
    print(solve(L, R))

if __name__ == '__main__':
    main()

