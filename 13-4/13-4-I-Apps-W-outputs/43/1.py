
def get_unique_code_length(promo_codes):
    unique_codes = set(promo_codes)
    for i in range(len(promo_codes[0])):
        if len(unique_codes) == 1:
            return i
        unique_codes = {code[:i] + code[i+1:] for code in unique_codes}
    return len(promo_codes[0])

def get_max_errors(promo_codes):
    return len(promo_codes[0]) - get_unique_code_length(promo_codes)

if __name__ == '__main__':
    n = int(input())
    promo_codes = []
    for _ in range(n):
        promo_codes.append(input())
    print(get_max_errors(promo_codes))

