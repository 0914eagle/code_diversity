def is_bored(S):
    
    count = 0
    for word in S.split("."):
        for word in word.split("?"):
            for word in word.split("!"):
                if word.strip().startswith("I"):
                    count += 1
    return count
