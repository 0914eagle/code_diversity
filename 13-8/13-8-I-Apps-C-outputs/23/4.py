
def is_equivalent(program1, program2):
    # Tokenize the programs into a list of tokens
    tokens1 = tokenize(program1)
    tokens2 = tokenize(program2)
    
    # Check if the tokens are the same
    if tokens1 != tokens2:
        return "not equal"
    
    # Check if the programs are equivalent
    if is_equivalent_helper(tokens1, tokens2):
        return "equal"
    else:
        return "not equal"

def tokenize(program):
    # Tokenize the program into a list of tokens
    tokens = []
    for char in program:
        if char.isdigit():
            tokens.append(int(char))
        elif char in ["[", "]", ",", "("]:
            tokens.append(char)
    
    return tokens

def is_equivalent_helper(tokens1, tokens2):
    # Base case: if the tokens are the same, the programs are equivalent
    if tokens1 == tokens2:
        return True
    
    # Recursive case: if the first token is a list, check if the rest of the tokens are equivalent
    if tokens1[0] == "[":
        list1 = tokens1[1:-1]
        list2 = tokens2[1:-1]
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if not is_equivalent_helper(list1[i], list2[i]):
                return False
        return True
    
    # Recursive case: if the first token is a function, check if the rest of the tokens are equivalent
    if tokens1[0] in ["concat", "shuffle", "sorted"]:
        func1 = tokens1[0]
        args1 = tokens1[1:]
        func2 = tokens2[0]
        args2 = tokens2[1:]
        if len(args1) != len(args2):
            return False
        for i in range(len(args1)):
            if not is_equivalent_helper(args1[i], args2[i]):
                return False
        return True
    
    # Base case: if the tokens are not equivalent, the programs are not equivalent
    return False

