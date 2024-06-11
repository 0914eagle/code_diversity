def is_bored(S):
    
    # your code here
    # print(S.split("."))
    count = 0
    for i in S.split("."):
        if i.startswith("I"):
            count += 1
    return count


if __