


def triples_sum_to_zero(l: list):
    
    # Your code here
    l.sort()
    for i in range(len(l)-2):
        if l[i]==0:
            return True
        for j in range(i+1, len(l)-1):
            if l[i]+l[j]==-l[i+1]:
                return True
    return False

