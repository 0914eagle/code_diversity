def skjkasdkd(lst):
    
    lst = sorted(lst)
    for i in range(len(lst)):
        lst[i] = lst[i] % 10
    lst = [int(x) for x in str(sum(lst))]
    return sum(lst)

if __name__ == "__main__":
    lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]
    print(skjkasdkd(lst))