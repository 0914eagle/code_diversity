
def get_triplets_count(k, s):
    count = 0
    for i in range(k+1):
        for j in range(i+1):
            if i+j == s:
                count += 1
    return count

