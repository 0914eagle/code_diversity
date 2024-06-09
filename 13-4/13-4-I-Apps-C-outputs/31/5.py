
def pre_print(tree):
    output(tree.value)
    if tree.left != null: pre_print(tree.left)
    if tree.right != null: pre_print(tree.right)

def in_print(tree):
    if tree.left != null: in_print(tree.left)
    output(tree.value)
    if tree.right != null: in_print(tree.right)

def post_print(tree):
    if tree.left != null: post_print(tree.left)
    if tree.right != null: post_print(tree.right)
    output(tree.value)

def find_reconstruction(pre_output, in_output, post_output):
    # find the first tree with the given preorder, inorder, and postorder outputs
    # return the reconstruction of Anatoly's code and the first tree
    pass

if __name__ == '__main__':
    pre_output = input()
    in_output = input()
    post_output = input()
    reconstruction, tree = find_reconstruction(pre_output, in_output, post_output)
    print(reconstruction)
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())

