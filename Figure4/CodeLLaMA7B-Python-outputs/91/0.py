def is_bored(S):
    
    # your code here
    count = 0
    for i in range(len(S)-1):
        if S[i] == "I" and S[i+1] == " ":
            count += 1
    return count


