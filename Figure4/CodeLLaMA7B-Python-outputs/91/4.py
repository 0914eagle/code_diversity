def is_bored(S):
    
    # Your code here
    count = 0
    for i in S.split("."):
        if i.strip().startswith("I"):
            count += 1
    return count


