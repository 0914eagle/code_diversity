
def f1(n):
    # f1 function to input the three-digit integer n
    n = int(input())
    return n

def f2(n):
    # f2 function to replace each occurrence of 1 with 9 and each occurrence of 9 with 1 in n
    n_str = str(n)
    n_list = list(n_str)
    for i in range(len(n_list)):
        if n_list[i] == '1':
            n_list[i] = '9'
        elif n_list[i] == '9':
            n_list[i] = '1'
    n_str = ''.join(n_list)
    n = int(n_str)
    return n

if __name__ == '__main__':
    n = f1(n)
    print(f2(n))

