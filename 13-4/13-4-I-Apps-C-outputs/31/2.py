
def get_reconstructions(pre_output, in_output, post_output):
    # Find all possible combinations of Pre, In, and Post calls
    combinations = []
    for pre_calls in range(0, 3):
        for in_calls in range(0, 3):
            for post_calls in range(0, 3):
                if pre_calls + in_calls + post_calls == 6:
                    combinations.append([pre_calls, in_calls, post_calls])
    
    # Iterate through all possible combinations and find the first tree that generates the observed outputs
    reconstructions = []
    for combination in combinations:
        pre_calls = combination[0]
        in_calls = combination[1]
        post_calls = combination[2]
        pre_print = "".join(pre_output[:pre_calls])
        in_print = "".join(in_output[:in_calls])
        post_print = "".join(post_output[:post_calls])
        tree = find_tree(pre_print, in_print, post_print)
        if tree:
            reconstructions.append([combination, tree])
    
    return reconstructions

def find_tree(pre_print, in_print, post_print):
    # Find all possible trees that generate the observed outputs
    trees = []
    for tree in generate_trees(pre_print):
        if tree_prints_match(tree, pre_print, in_print, post_print):
            trees.append(tree)
    
    # Return the first tree with the alphabetically first preorder print
    if len(trees) > 0:
        return sorted(trees, key=lambda x: x[0])[0]
    else:
        return None

def generate_trees(pre_print):
    # Generate all possible trees with the given preorder print
    if len(pre_print) == 0:
        yield []
    else:
        for i in range(1, len(pre_print)):
            for left in generate_trees(pre_print[:i]):
                for right in generate_trees(pre_print[i:]):
                    yield [pre_print[i]] + left + right

def tree_prints_match(tree, pre_print, in_print, post_print):
    # Check if the given tree generates the observed outputs
    if len(tree) == 0:
        return pre_print == "" and in_print == "" and post_print == ""
    else:
        root = tree[0]
        left = tree[1:]
        return (pre_print.startswith(root) and in_print.startswith(root) and post_print.startswith(root) and
                tree_prints_match(left, pre_print[1:], in_print[1:], post_print[1:]))

if __name__ == '__main__':
    pre_output = "HFBIGEDCJA"
    in_output = "BIGEDCJFAH"
    post_output = "BIGEDCJFAH"
    reconstructions = get_reconstructions(pre_output, in_output, post_output)
    for reconstruction in reconstructions:
        print(reconstruction[0])
        print(reconstruction[1][0])
        print(reconstruction[1][1])
        print(reconstruction[1][2])

