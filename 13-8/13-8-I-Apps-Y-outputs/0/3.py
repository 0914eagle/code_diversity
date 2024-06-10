
def get_list(x):
    # find all factors of x
    factors = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            factors.append(i)
            if x // i != i:
                factors.append(x // i)
    
    # sort factors in descending order
    factors.sort(reverse=True)
    
    # create a list of factors with 1 added to each factor
    factor_list = [i + 1 for i in factors]
    
    # multiply all factors together
    product = 1
    for i in factor_list:
        product *= i
    
    # check if the product is equal to x
    if product == x:
        return factor_list
    else:
        return []

def get_points(x):
    factor_list = get_list(x)
    if factor_list:
        return len(factor_list)
    else:
        return 0

def main():
    x = int(input())
    print(get_points(x))

if __name__ == '__main__':
    main()

