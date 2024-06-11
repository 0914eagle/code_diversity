def is_bored(S):
    
    count = 0
    for i in S.split("."):
        for j in i.split("?"):
            for k in j.split("!"):
                if k.strip().startswith("I"):
                    count += 1
    return count
