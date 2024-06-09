
def get_min_operations(balances):
    n = len(balances)
    operations = 0
    for i in range(n):
        balance = balances[i]
        while balance != 0:
            operations += 1
            if balance > 0:
                balance -= 1
                balances[(i+1)%n] += 1
            else:
                balance += 1
                balances[(i-1)%n] -= 1
    return operations

