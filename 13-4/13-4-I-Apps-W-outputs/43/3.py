
def get_unique_code_length(promo_codes):
    unique_codes = set(promo_codes)
    return len(unique_codes)

def get_max_mistakes(promo_codes):
    unique_codes = set(promo_codes)
    max_mistakes = 0
    for code in unique_codes:
        for i in range(len(code)):
            for j in range(10):
                if code[:i] + str(j) + code[i+1:] in unique_codes:
                    max_mistakes = max(max_mistakes, i)
    return max_mistakes

def main():
    n = int(input())
    promo_codes = []
    for i in range(n):
        promo_codes.append(input())
    print(get_max_mistakes(promo_codes))

if __name__ == '__main__':
    main()

