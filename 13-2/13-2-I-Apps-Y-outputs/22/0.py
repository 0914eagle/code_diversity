
def f1(X):
    balance = 100
    years = 0
    while balance < X:
        balance = balance * 1.01
        years += 1
    return years

