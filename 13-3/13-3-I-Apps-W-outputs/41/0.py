
def get_maximum_balance(balance):
    if balance >= 0:
        return balance
    else:
        balance_str = str(balance)
        if len(balance_str) == 1:
            return 0
        else:
            return max(int(balance_str[:-1]), int(balance_str[:-2]))

