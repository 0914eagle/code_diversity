
def get_max_k(promo_codes):
    k = 0
    for i in range(len(promo_codes[0])):
        for pc in promo_codes:
            if pc[i] != pc[0]:
                k += 1
                break
        if k > len(promo_codes[0]):
            break
    return k

def get_unique_promo_codes(promo_codes, k):
    unique_codes = []
    for pc in promo_codes:
        pc_list = list(pc)
        for i in range(len(pc_list)):
            if pc_list[i] != pc_list[0]:
                pc_list[i] = 'X'
        unique_codes.append(''.join(pc_list))
    return unique_codes

def main():
    n = int(input())
    promo_codes = []
    for i in range(n):
        promo_codes.append(input())
    k = get_max_k(promo_codes)
    unique_codes = get_unique_promo_codes(promo_codes, k)
    print(k)
    for code in unique_codes:
        print(code)

if __name__ == '__main__':
    main()

