
def pre_print(t):
    output(t.value)
    if t.left != null: pre_print(t.left)
    if t.right != null: pre_print(t.right)

def in_print(t):
    if t.left != null: pre_print(t.left)
    output(t.value)
    if t.right != null: pre_print(t.right)

def post_print(t):
    if t.left != null: pre_print(t.left)
    if t.right != null: pre_print(t.right)
    output(t.value)

def find_reconstructions(pre_output, in_output, post_output):
    # Find all possible reconstructions of Anatoly's code
    reconstructions = []
    for pre_call in ["Pre", "In", "Post"]:
        for in_call in ["Pre", "In", "Post"]:
            for post_call in ["Pre", "In", "Post"]:
                if pre_call != in_call and pre_call != post_call and in_call != post_call:
                    reconstructions.append([pre_call, in_call, post_call])
    
    # Find the first tree that generates the observed outputs
    for reconstruction in reconstructions:
        pre_calls = [reconstruction[0], reconstruction[2]]
        in_calls = [reconstruction[1], reconstruction[2]]
        post_calls = [reconstruction[0], reconstruction[1]]
        pre_tree = find_tree(pre_calls, pre_output)
        in_tree = find_tree(in_calls, in_output)
        post_tree = find_tree(post_calls, post_output)
        if pre_tree and in_tree and post_tree:
            return reconstruction, pre_tree, in_tree, post_tree
    
    return None, None, None, None

def find_tree(calls, output):
    # Find the first tree that generates the observed outputs
    for tree in all_trees:
        if calls[0] == "Pre":
            pre_print(tree)
        elif calls[0] == "In":
            in_print(tree)
        else:
            post_print(tree)
        if output == "".join(tree.values()):
            return tree
    return None

def output(value):
    # Simulate the output statement
    print(value, end="")

if __name__ == '__main__':
    pre_output = input("Preorder print: ")
    in_output = input("Inorder print: ")
    post_output = input("Postorder print: ")
    reconstruction, pre_tree, in_tree, post_tree = find_reconstructions(pre_output, in_output, post_output)
    if reconstruction:
        print("Reconstruction:", " ".join(reconstruction))
        print("Preorder print:", "".join(pre_tree.values()))
        print("Inorder print:", "".join(in_tree.values()))
        print("Postorder print:", "".join(post_tree.values()))
    else:
        print("No reconstruction found.")

