
def is_same_group(x, y):
    # Define the groups
    group1 = [1, 2, 3, 4, 5]
    group2 = [6, 7, 8, 9, 10]
    group3 = [11, 12]

    # Check if x and y are in the same group
    if x in group1 and y in group1:
        return True
    elif x in group2 and y in group2:
        return True
    elif x in group3 and y in group3:
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

