def simplify(x, n):
    
    if x == '0':
        return True
    if x.find('/') == -1:
        return x == str(int(x) * int(n))
    else:
        x_num, x_den = x.split('/')
        n_num, n_den = n.split('/')
        if int(x_num) * int(n_den) == int(x_den) * int(n_num):
            return simplify(x_den, n_num)
        else:
            return False


if __name__ == '__main__':
    print(simplify('1/5', '5/1'))
    print(simplify('1/6', '2/1'))
    print(simplify('7/10', '10/2'))
