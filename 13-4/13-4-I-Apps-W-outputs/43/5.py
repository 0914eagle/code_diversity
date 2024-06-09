
def get_unique_code(n, codes):
    unique_code = ""
    for i in range(n):
        unique_code += str(i)
    return unique_code

def get_k_mistakes(n, codes, k):
    unique_code = get_unique_code(n, codes)
    for i in range(k):
        for j in range(n):
            if codes[j] == unique_code[:n-i-1] + str(j) + unique_code[n-i:]:
                return k
    return -1

def main():
    n = int(input())
    codes = []
    for i in range(n):
        codes.append(input())
    k = get_k_mistakes(n, codes, n-1)
    print(k)

if __name__ == '__main__':
    main()

