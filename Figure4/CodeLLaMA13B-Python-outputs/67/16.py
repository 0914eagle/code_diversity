def fruit_distribution(s,n):
    
    # your code here
    # split the string into a list
    fruit_list = s.split()
    # remove the word 'and' from the list
    fruit_list.pop(2)
    # convert the list to integers
    fruit_list = [int(i) for i in fruit_list]
    # return the difference between the total number of the fruits and the number of the apples and oranges
    return n - sum(fruit_list)


if __name__ == '__main__':
    print(fruit_distribution("5 apples and 6 oranges", 19))
    print(fruit_distribution("0 apples and 1 oranges",3))
    print(fruit_distribution("2 apples and 3 oranges", 100))
    print(fruit_distribution("100 apples and 1 oranges",120))
