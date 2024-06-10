
def input_data():
    n, m = map(int, input().split())
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))
    return n, m, y1, y2

def count_destructible_spaceships(n, m, y1, y2):
    count = 0
    for i in range(n):
        for j in range(m):
            if y1[i] == y2[j]:
                count += 1
    return count

def main():
    n, m, y1, y2 = input_data()
    print(count_destructible_spaceships(n, m, y1, y2))

if __name__ == '__main__':
    main()

