
def f1(n, a):
    # find the pile with the most stones
    max_pile = 0
    for i in range(n):
        if a[i] > a[max_pile]:
            max_pile = i
    
    # check if the pile with the most stones has only one stone
    if a[max_pile] == 1:
        return "cslnb"
    
    # check if the pile with the most stones has two stones
    if a[max_pile] == 2:
        # find the pile with the second most stones
        second_max_pile = 0
        for i in range(n):
            if i != max_pile and a[i] > a[second_max_pile]:
                second_max_pile = i
        
        # check if the pile with the second most stones has only one stone
        if a[second_max_pile] == 1:
            return "sjfnb"
    
    # if the pile with the most stones has more than two stones, Tokitsukaze can make a valid move
    return "sjfnb"

def f2(n, a):
    # find the pile with the most stones
    max_pile = 0
    for i in range(n):
        if a[i] > a[max_pile]:
            max_pile = i
    
    # check if the pile with the most stones has only one stone
    if a[max_pile] == 1:
        return "cslnb"
    
    # check if the pile with the most stones has two stones
    if a[max_pile] == 2:
        # find the pile with the second most stones
        second_max_pile = 0
        for i in range(n):
            if i != max_pile and a[i] > a[second_max_pile]:
                second_max_pile = i
        
        # check if the pile with the second most stones has only one stone
        if a[second_max_pile] == 1:
            return "sjfnb"
    
    # if the pile with the most stones has more than two stones, Tokitsukaze can make a valid move
    return "sjfnb"

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

