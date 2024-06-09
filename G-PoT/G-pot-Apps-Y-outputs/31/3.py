
def food_status(X, A, B):
    best_by_date = A + X
    if B <= best_by_date:
        return "delicious"
    elif B > best_by_date + 1:
        return "dangerous"
    else:
        return "safe"

X, A, B = map(int, input().split())
print(food_status(X, A, B))
