
def is_bored(S: str) -> int:
    
    return len([sentence for sentence in S.split(".") if sentence.strip().startswith("I")])

