
def get_happiness(n, cake):
    # Initialize variables
    happiness = 0
    rows = [[] for _ in range(n)]
    cols = [[] for _ in range(n)]
    
    # Fill the rows and columns with the chocolates
    for i in range(n):
        for j in range(n):
            if cake[i][j] == "C":
                rows[i].append(j)
                cols[j].append(i)
    
    # Count the happiness
    for i in range(n):
        for j in range(n):
            for k in range(j+1, n):
                if rows[i][j] == cols[i][k]:
                    happiness += 1
    
    return happiness

def main():
    n = int(input())
    cake = [input() for _ in range(n)]
    print(get_happiness(n, cake))

if __name__ == '__main__':
    main()

