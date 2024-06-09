
def is_same_group(x, y):
    if x in [1, 2, 3] and y in [1, 2, 3]:
        return True
    elif x in [4, 5, 6] and y in [4, 5, 6]:
        return True
    elif x in [7, 8, 9] and y in [7, 8, 9]:
        return True
    elif x in [10, 11, 12] and y in [10, 11, 12]:
        return True
    else:
        return False

def main():
    x, y = map(int, input().split())
    if is_same_group(x, y):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

