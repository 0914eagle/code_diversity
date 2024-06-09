
def solve(A):
    count = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j and A[j] % A[i] == 0:
                break
        else:
            count += 1
    return count

