
def restore_expression(digits):
    n = len(digits)
    for i in range(1, n):
        for j in range(i+1, n):
            a_str = digits[:i]
            b_str = digits[i:j]
            c_str = digits[j:]
            if (a_str[0] != '0' or len(a_str) == 1) and (b_str[0] != '0' or len(b_str) == 1) and (c_str[0] != '0' or len(c_str) == 1):
                a = int(a_str)
                b = int(b_str)
                c = int(c_str)
                if a + b == c:
                    return f"{a_str}+{b_str}={c_str}"

if __name__ == "__main__":
    digits = input().strip()
    print(restore_expression(digits))
