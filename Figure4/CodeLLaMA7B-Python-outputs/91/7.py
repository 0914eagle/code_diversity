def is_bored(S):
    
    # your code here
    count = 0
    for i in S.split("."):
        if i.strip().startswith("I"):
            count += 1
    return count


if __name__ == "__main__":
