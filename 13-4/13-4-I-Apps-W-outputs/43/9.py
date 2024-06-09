
def get_unique_promo_codes(promo_codes):
    unique_codes = set()
    for code in promo_codes:
        unique_codes.add(code)
    return unique_codes

def get_max_errors(promo_codes, k):
    unique_codes = get_unique_promo_codes(promo_codes)
    for code in unique_codes:
        for i in range(len(code)):
            for j in range(10):
                if code[i] != str(j):
                    modified_code = code[:i] + str(j) + code[i+1:]
                    if modified_code in unique_codes:
                        return k
    return k - 1

def main():
    n = int(input())
    promo_codes = []
    for i in range(n):
        promo_codes.append(input())
    k = len(promo_codes[0])
    print(get_max_errors(promo_codes, k))

if __name__ == '__main__':
    main()

