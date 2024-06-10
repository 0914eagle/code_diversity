
def get_sum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum -= i
        else:
            sum += i
    return sum

def get_sum_all(n_list):
    result = []
    for n in n_list:
        result.append(get_sum(n))
    return result

if __name__ == '__main__':
    t = int(input())
    n_list = []
    for i in range(t):
        n_list.append(int(input()))
    print(get_sum_all(n_list))

