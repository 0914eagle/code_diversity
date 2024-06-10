
def get_number_of_bridges(a, b, c):
    # Initialize a 2D array to store the number of bridges between each pair of islands
    num_bridges = [[0 for _ in range(a)] for _ in range(a)]
    
    # Populate the array with the number of bridges between each pair of islands
    for i in range(a):
        for j in range(i+1, a):
            if i != j:
                num_bridges[i][j] = 1
    
    # Add the number of bridges between blue and purple clusters
    for i in range(b):
        for j in range(c):
            if i != j:
                num_bridges[i][j + a] = 1
    
    # Calculate the total number of bridges
    total_bridges = 0
    for row in num_bridges:
        total_bridges += sum(row)
    
    # Return the total number of bridges modulo 998 244 353
    return total_bridges % 998244353

def main():
    a, b, c = map(int, input().split())
    print(get_number_of_bridges(a, b, c))

if __name__ == '__main__':
    main()

