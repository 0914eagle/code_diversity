
def get_number_of_bridges(a, b, c):
    # Initialize a list to store the number of bridges for each color
    num_bridges = [0, 0, 0]
    
    # Loop through each color and calculate the number of bridges
    for i in range(3):
        num_bridges[i] = (a + b + c - 3) * (a + b + c - 2) // 2
    
    # Return the total number of bridges modulo 998244353
    return sum(num_bridges) % 998244353

def main():
    a, b, c = map(int, input().split())
    print(get_number_of_bridges(a, b, c))

if __name__ == '__main__':
    main()

