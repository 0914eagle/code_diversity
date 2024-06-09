
def get_k_rounding(n, k):
    if k == 0:
        return n
    
    # convert n to string
    n_str = str(n)
    
    # find the index of the first non-zero digit in n
    first_non_zero_index = 0
    for i in range(len(n_str)):
        if n_str[i] != '0':
            first_non_zero_index = i
            break
    
    # add zeros to the end of n until it has k or more zeros
    while len(n_str) - first_non_zero_index < k:
        n_str += '0'
    
    # convert n_str back to int and return it
    return int(n_str)

def main():
    n, k = map(int, input().split())
    print(get_k_rounding(n, k))

if __name__ == '__main__':
    main()

