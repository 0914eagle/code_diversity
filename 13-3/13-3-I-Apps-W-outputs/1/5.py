
def count_attacking_pairs(bishops):
    n = len(bishops)
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if bishops[i][0] + bishops[i][1] == bishops[j][0] + bishops[j][1] or bishops[i][0] - bishops[i][1] == bishops[j][0] - bishops[j][1]:
                pairs += 1
    return pairs

def main():
    n = int(input())
    bishops = []
    for i in range(n):
        x, y = map(int, input().split())
        bishops.append([x, y])
    print(count_attacking_pairs(bishops))

if __name__ == '__main__':
    main()

