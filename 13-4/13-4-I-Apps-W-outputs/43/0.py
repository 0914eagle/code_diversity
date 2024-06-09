
def get_unique_code(promo_codes):
    unique_code = ""
    for code in promo_codes:
        if code not in unique_code:
            unique_code += code
    return unique_code

def get_max_k(promo_codes, k):
    unique_code = get_unique_code(promo_codes)
    for i in range(k):
        if len(unique_code) == 1:
            return k
        unique_code = get_unique_code(unique_code)
    return k

def main():
    n = int(input())
    promo_codes = []
    for i in range(n):
        promo_codes.append(input())
    k = get_max_k(promo_codes, len(promo_codes[0]))
    print(k)

if __name__ == '__main__':
    main()

