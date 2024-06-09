
def count_binary_relations(n):
    count = 0
    for i in range(1, n+1):
        count += (n-i) * i
    return count % (10**9 + 7)

