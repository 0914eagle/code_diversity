
def input_data():
    n = int(input())
    c = [int(i) for i in input().split()]
    return n, c

def is_possible(n, c):
    # Initialize a list to store the number of nodes in each subtree
    num_nodes = [0] * (n + 1)
    num_nodes[0] = 1

    # Iterate through the input array and calculate the number of nodes in each subtree
    for i in range(1, n + 1):
        num_nodes[i] = num_nodes[i - 1] + c[i - 1]

    # Check if the number of nodes in each subtree is greater than or equal to 2
    for i in range(1, n + 1):
        if num_nodes[i] < 2:
            return False

    return True

def main():
    n, c = input_data()
    print("YES") if is_possible(n, c) else print("NO")

if __name__ == '__main__':
    main()

