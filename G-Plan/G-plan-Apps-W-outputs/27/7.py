
def restore_expression(input_string):
    for i in range(1, len(input_string)):
        for j in range(i+1, len(input_string)):
            a = input_string[:i]
            b = input_string[i:j]
            c = input_string[j:]
            if (a[0] != '0' or len(a) == 1) and (b[0] != '0' or len(b) == 1) and (c[0] != '0' or len(c) == 1):
                if int(a) + int(b) == int(c):
                    return a + '+' + b + '=' + c

if __name__ == "__main__":
    input_string = input().strip()
    result = restore_expression(input_string)
    print(result)
