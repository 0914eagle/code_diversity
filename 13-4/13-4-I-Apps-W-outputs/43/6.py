
def get_max_k(promo_codes):
    k = 0
    for i in range(len(promo_codes[0])):
        for pc in promo_codes:
            if pc[i] != pc[0]:
                break
        else:
            k += 1
    return k

def get_unique_promo_codes(promo_codes, k):
    unique_codes = []
    for pc in promo_codes:
        for i in range(len(pc)):
            if pc[i] != pc[0]:
                break
        else:
            unique_codes.append(pc)
    return unique_codes

def main():
    n = int(input())
    promo_codes = []
    for i in range(n):
        promo_codes.append(input())
    k = get_max_k(promo_codes)
    unique_codes = get_unique_promo_codes(promo_codes, k)
    print(k)
    for pc in unique_codes:
        print(pc)

if __name__ == '__main__':
    main()

