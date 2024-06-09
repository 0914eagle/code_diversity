
def get_minimum_operations(balances):
    n = len(balances)
    operations = 0
    for i in range(n):
        while balances[i] != 0:
            j = (i + 1) % n
            if balances[i] > 0 and balances[j] < 0:
                balances[i] += balances[j]
                balances[j] = 0
            else:
                balances[j] += balances[i]
                balances[i] = 0
            operations += 1
    return operations

