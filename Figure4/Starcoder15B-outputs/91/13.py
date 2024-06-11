def is_bored(S):
    
    return len([x for x in S.split(".") if x.startswith("I")])

