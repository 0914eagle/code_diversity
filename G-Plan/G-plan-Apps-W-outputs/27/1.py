
def restore_expression(digits):
    n = len(digits)
    for i in range(1, n):
        for j in range(i+1, n):
            a = digits[:i]
            b = digits[i:j]
            c = digits[j:]
            if (a[0] != '0' or len(a) == 1) and (b[0] != '0' or len(b) == 1) and (c[0] != '0' or len(c) == 1):
                if int(a) + int(b) == int(c):
                    return f"{a}+{b}={c}"

if __name__ == "__main__":
    digits = input().strip()
    print(restore_expression(digits))
