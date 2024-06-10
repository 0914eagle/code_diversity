
def read_input():
    n = int(input())
    cake = []
    for _ in range(n):
        cake.append(input())
    return n, cake

def count_pairs(cake):
    n = len(cake)
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if cake[i][j] == 'C' and cake[j][i] == 'C':
                pairs += 1
    return pairs

def main():
    n, cake = read_input()
    print(count_pairs(cake))

if __name__ == '__main__':
    main()

