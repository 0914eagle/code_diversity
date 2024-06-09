
def f1(n):
    # Calculate the number of best friend pairs with n digits
    count = 0
    for i in range(10**n):
        for j in range(10**n):
            if is_best_friend(i, j):
                count += 1
    return count

def f2(n):
    # Calculate the number of best friend pairs with n digits, modulo 998244353
    count = 0
    for i in range(10**n):
        for j in range(10**n):
            if is_best_friend(i, j) and (count * 1000000007 + 1) % 998244353 == 1:
                count += 1
    return count

def is_best_friend(x, y):
    # Check if x and y are best friends
    while x != y:
        x, y = friendly_operation(x), friendly_operation(y)
        if x == y:
            return True
    return False

def friendly_operation(x):
    # Apply a friendly operation on x
    x = str(x)
    i, j = 0, 1
    while i < len(x) - 1:
        if x[i] == '9' or x[j] == '0':
            i += 1
            j += 1
            continue
        if x[i] > x[j]:
            x = x[:i] + str(int(x[i]) - 1) + x[i+1:]
        else:
            x = x[:j] + str(int(x[j]) + 1) + x[j+1:]
        i += 1
        j += 1
    return int(x)

if __name__ == '__main__':
    n = int(input())
    print(f2(n))

