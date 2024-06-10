
def restore_expression(input_str):
    n = len(input_str)
    for i in range(1, n):
        for j in range(i + 1, n):
            a = int(input_str[:i])
            b = int(input_str[i:j])
            c = int(input_str[j:])
            if str(a) == input_str[:i] and str(b) == input_str[i:j] and str(c) == input_str[j:] and a + b == c:
                return f"{a}+{b}={c}"

if __name__ == "__main__":
    input_str = input().strip()
    print(restore_expression(input_str))
