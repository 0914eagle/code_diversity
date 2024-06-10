
def read_input():
    n = int(input())
    cake = []
    for _ in range(n):
        cake.append(input())
    return n, cake

def count_happiness(cake):
    n = len(cake)
    happiness = 0
    for i in range(n):
        for j in range(i+1, n):
            if cake[i][j] == 'C' and cake[j][i] == 'C':
                happiness += 1
    return happiness

def main():
    n, cake = read_input()
    print(count_happiness(cake))

if __name__ == '__main__':
    main()

