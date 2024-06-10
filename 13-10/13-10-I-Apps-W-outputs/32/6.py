
def get_happiness(cake):
    n = len(cake)
    happiness = 0
    for i in range(n):
        for j in range(i+1, n):
            if cake[i][j] == 'C' and cake[j][i] == 'C':
                happiness += 1
    return happiness

def get_cake(n):
    cake = []
    for i in range(n):
        cake.append(input().strip())
    return cake

if __name__ == '__main__':
    n = int(input())
    cake = get_cake(n)
    happiness = get_happiness(cake)
    print(happiness)

