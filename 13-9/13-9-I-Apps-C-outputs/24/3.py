
def is_possible(n, c_list):
    # Initialize a dictionary to store the number of nodes in each subtree
    subtree_size = {}
    for i in range(n):
        subtree_size[i] = c_list[i]

    # Initialize a set to store the nodes that have at least two sons
    nodes_with_two_sons = set()

    # Loop through the nodes and check if they have at least two sons
    for i in range(n):
        if subtree_size[i] > 1:
            nodes_with_two_sons.add(i)

    # If there is no node with at least two sons, it is not possible to build a tree following Iahub's restrictions
    if len(nodes_with_two_sons) == 0:
        return False

    # Loop through the nodes and check if they are connected to at least one node with at least two sons
    for i in range(n):
        if i not in nodes_with_two_sons:
            connected_to_two_sons = False
            for j in range(n):
                if j in nodes_with_two_sons and subtree_size[j] > 1 and i in subtree_size[j]:
                    connected_to_two_sons = True
                    break
            if not connected_to_two_sons:
                return False

    return True

def main():
    n = int(input())
    c_list = list(map(int, input().split()))
    print(is_possible(n, c_list))

if __name__ == '__main__':
    main()

