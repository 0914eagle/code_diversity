def exchange(lst1, lst2):
    
    # Your code here
    lst1_even = []
    lst2_even = []
    for i in lst1:
        if i % 2 == 0:
            lst1_even.append(i)
    for i in lst2:
        if i % 2 == 0:
            lst2_even.append(i)
    if lst1_even == lst2_even:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    lst1 = [1, 2, 3, 4]
    lst2 = [1, 2, 3, 4]
    print(exchange(lst1, lst2))
