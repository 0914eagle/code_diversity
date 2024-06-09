
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

def find_reconstruction(pre_output, in_output, post_output):
    # Find the possible calls to pre_print, in_print, and post_print
    pre_calls = []
    in_calls = []
    post_calls = []
    for i in range(len(pre_output)):
        if pre_output[i] == 'P':
            pre_calls.append(i)
        elif in_output[i] == 'I':
            in_calls.append(i)
        elif post_output[i] == 'P':
            post_calls.append(i)
    
    # Find the possible trees that could have generated the output
    trees = []
    for pre_call in pre_calls:
        for in_call in in_calls:
            for post_call in post_calls:
                if pre_call < in_call and in_call < post_call:
                    tree = [pre_output[pre_call], in_output[in_call], post_output[post_call]]
                    trees.append(tree)
    
    # Find the alphabetically first tree
    first_tree = None
    for tree in trees:
        if first_tree == None or tree < first_tree:
            first_tree = tree
    
    return first_tree

if __name__ == '__main__':
    pre_output = input("Preorder output: ")
    in_output = input("Inorder output: ")
    post_output = input("Postorder output: ")
    reconstruction = find_reconstruction(pre_output, in_output, post_output)
    print(reconstruction)

