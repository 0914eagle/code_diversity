
def parse_input(n):
    cake = []
    for _ in range(n):
        row = input()
        cake.append(list(row))
    return cake

def count_happiness(cake):
    n = len(cake)
    happiness = 0
    for i in range(n):
        for j in range(n):
            if cake[i][j] == 'C':
                for k in range(n):
                    if cake[i][k] == 'C' and k != j:
                        happiness += 1
                    if cake[k][j] == 'C' and k != i:
                        happiness += 1
    return happiness

def main():
    n = int(input())
    cake = parse_input(n)
    print(count_happiness(cake))

if __name__ == '__main__':
    main()

