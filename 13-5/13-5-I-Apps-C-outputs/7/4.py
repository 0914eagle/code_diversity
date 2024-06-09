
def f1(n, a):
    # find the pile with the maximum number of stones
    max_pile = 0
    for i in range(n):
        if a[i] > a[max_pile]:
            max_pile = i
    
    # check if the maximum pile has only one stone
    if a[max_pile] == 1:
        return "sjfnb"
    
    # check if the maximum pile has two or more stones
    else:
        # find the pile with the second maximum number of stones
        sec_max_pile = 0
        for i in range(n):
            if i != max_pile and a[i] > a[sec_max_pile]:
                sec_max_pile = i
        
        # check if the second maximum pile has only one stone
        if a[sec_max_pile] == 1:
            return "cslnb"
        
        # check if the second maximum pile has two or more stones
        else:
            return "sjfnb"

def f2(n, a):
    # find the pile with the minimum number of stones
    min_pile = 0
    for i in range(n):
        if a[i] < a[min_pile]:
            min_pile = i
    
    # check if the minimum pile has only one stone
    if a[min_pile] == 1:
        return "cslnb"
    
    # check if the minimum pile has two or more stones
    else:
        # find the pile with the second minimum number of stones
        sec_min_pile = 0
        for i in range(n):
            if i != min_pile and a[i] < a[sec_min_pile]:
                sec_min_pile = i
        
        # check if the second minimum pile has only one stone
        if a[sec_min_pile] == 1:
            return "sjfnb"
        
        # check if the second minimum pile has two or more stones
        else:
            return "cslnb"

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

