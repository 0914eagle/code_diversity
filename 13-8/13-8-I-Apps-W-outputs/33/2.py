
def get_min_operations(balances):
    n = len(balances)
    operations = 0
    for i in range(n):
        while balances[i] != 0:
            operations += 1
            j = (i + 1) % n
            if balances[i] > 0:
                balances[j] += balances[i]
                balances[i] = 0
            else:
                balances[j] -= balances[i]
                balances[i] = 0
    return operations

