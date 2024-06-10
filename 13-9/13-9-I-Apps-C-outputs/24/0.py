
def is_rooted_tree_possible(n, c):
    # Initialize a list to store the number of nodes in each subtree
    subtree_sizes = [0] * (n + 1)
    subtree_sizes[0] = 1

    # Iterate through the input array and calculate the number of nodes in each subtree
    for i in range(n):
        subtree_sizes[i + 1] = subtree_sizes[i] + c[i]

    # Check if the number of nodes in the last subtree is greater than or equal to the number of nodes in the first subtree
    if subtree_sizes[-1] < subtree_sizes[0]:
        return False

    # Check if the number of nodes in each internal node is greater than or equal to 2
    for i in range(1, n):
        if subtree_sizes[i] < 2:
            return False

    return True

def main():
    n = int(input())
    c = list(map(int, input().split()))
    print("YES") if is_rooted_tree_possible(n, c) else print("NO")

if __name__ == '__main__':
    main()

