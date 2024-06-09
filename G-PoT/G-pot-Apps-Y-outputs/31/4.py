
def check_food(X, A, B):
    if B <= A:
        print("delicious")
    elif B - A <= X:
        print("safe")
    else:
        print("dangerous")

# Input
X, A, B = map(int, input().split())

# Check the food
check_food(X, A, B)
