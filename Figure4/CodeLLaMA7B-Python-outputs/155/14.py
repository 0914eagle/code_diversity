def even_odd_count(num):
    
    # return (sum(int(i) % 2 == 0 for i in str(num)), sum(int(i) % 2 != 0 for i in str(num)))
    # return (sum(int(i) % 2 == 0 for i in str(num)), len(str(num)) - sum(int(i) % 2 == 0 for i in str(num)))
    # return (sum(int(i) % 2 == 0 for i in str(num)), len(str(num)) - sum(int(i) % 2 != 0 for i in str(num)))
    return (sum(int(i) % 2 == 0 for i in str(num)), len(str(num)) - sum(int(i) % 2 == 0 for i in str(num)))


if __name__ == '__main__':
    print(even_odd_count(123))
