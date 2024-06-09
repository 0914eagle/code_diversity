
def get_min_operations(balances):
    n = len(balances)
    operations = 0
    for i in range(n):
        while balances[i] != 0:
            operations += 1
            neighbor = (i + 1) % n
            balances[neighbor] += balances[i]
            balances[i] = 0
    return operations

