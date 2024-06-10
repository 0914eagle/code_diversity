
def get_happiness(n, cake):
    happiness = 0
    for i in range(n):
        for j in range(n):
            if cake[i][j] == "C":
                happiness += 1
                if i < n - 1 and cake[i + 1][j] == "C":
                    happiness += 1
                if j < n - 1 and cake[i][j + 1] == "C":
                    happiness += 1
    return happiness

def main():
    n = int(input())
    cake = []
    for i in range(n):
        cake.append(input())
    print(get_happiness(n, cake))

if __name__ == '__main__':
    main()

