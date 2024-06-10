
def calculate_result(x, y, z):
    if x > y:
        return "+"
    elif x < y:
        return "-"
    else:
        return "0"

def check_uncertainty(x, y, z):
    if z == 0:
        return calculate_result(x, y, z)
    else:
        for i in range(z + 1):
            for j in range(z + 1):
                k = z - i - j
                if calculate_result(x + i, y + j, k) != calculate_result(x + j, y + i, k):
                    return "?"
        return calculate_result(x, y, z)

if __name__ == '__main__':
    x, y, z = map(int, input().split())
    print(check_uncertainty(x, y, z))

