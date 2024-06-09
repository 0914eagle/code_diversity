
def get_minimum_operations(balances):
    n = len(balances)
    operations = 0
    for i in range(n):
        while balances[i] != 0:
            operations += 1
            neighbor = (i + 1) % n
            if balances[i] > 0:
                balances[neighbor] += balances[i]
                balances[i] = 0
            else:
                balances[i] += balances[neighbor]
                balances[neighbor] = 0
    return operations

