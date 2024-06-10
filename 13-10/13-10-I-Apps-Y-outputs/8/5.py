
def main():
    n = int(input())
    table = []
    for i in range(n):
        table.append([int(j) for j in input().split()])
    
    # Floyd-Warshall algorithm to find the shortest path between all pairs of vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])
    
    # Print the roads
    for i in range(n):
        for j in range(i+1, n):
            if table[i][j] != table[j][i]:
                print(i+1, j+1)

if __name__ == '__main__':
    main()

