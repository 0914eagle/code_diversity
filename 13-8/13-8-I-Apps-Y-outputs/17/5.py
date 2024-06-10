
def get_input():
    return int(input())

def solve(k):
    count = 0
    for i in range(1, k + 1, 2):
        for j in range(2, k + 1, 2):
            count += 1
    return count

def main():
    k = get_input()
    print(solve(k))

if __name__ == '__main__':
    main()

