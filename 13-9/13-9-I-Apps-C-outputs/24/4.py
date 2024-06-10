
def is_rooted_tree_possible(n, c_list):
    # Initialize a list to store the number of nodes in each subtree
    num_nodes_in_subtree = [0] * (n + 1)
    num_nodes_in_subtree[0] = 1

    # Iterate through the input list and calculate the number of nodes in each subtree
    for i in range(1, n + 1):
        num_nodes_in_subtree[i] = num_nodes_in_subtree[i - 1] + c_list[i - 1]

    # Initialize a list to store the number of internal nodes in each subtree
    num_internal_nodes_in_subtree = [0] * (n + 1)
    num_internal_nodes_in_subtree[1] = 1

    # Iterate through the input list and calculate the number of internal nodes in each subtree
    for i in range(2, n + 1):
        num_internal_nodes_in_subtree[i] = num_internal_nodes_in_subtree[i - 1] + 1

    # Initialize a list to store the number of leaves in each subtree
    num_leaves_in_subtree = [0] * (n + 1)
    num_leaves_in_subtree[0] = 1

    # Iterate through the input list and calculate the number of leaves in each subtree
    for i in range(1, n + 1):
        num_leaves_in_subtree[i] = num_leaves_in_subtree[i - 1] + c_list[i - 1]

    # Check if there is at least one rooted tree possible
    for i in range(1, n + 1):
        if num_nodes_in_subtree[i] == num_internal_nodes_in_subtree[i] and num_leaves_in_subtree[i] == c_list[i - 1]:
            return "YES"
    return "NO"

def main():
    n = int(input())
    c_list = list(map(int, input().split()))
    print(is_rooted_tree_possible(n, c_list))

if __name__ == '__main__':
    main()

