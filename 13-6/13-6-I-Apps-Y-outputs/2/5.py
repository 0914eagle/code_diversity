
def is_same_group(x, y):
    # Define the criteria for dividing the integers into groups
    group_1 = [1, 2, 3, 4, 5]
    group_2 = [6, 7, 8, 9, 10]
    group_3 = [11, 12]
    
    # Check if x and y belong to the same group
    if x in group_1 and y in group_1:
        return True
    elif x in group_2 and y in group_2:
        return True
    elif x in group_3 and y in group_3:
        return True
    else:
        return False

def main():
    # Accept input from the user
    x, y = map(int, input().split())
    
    # Check if x and y belong to the same group
    if is_same_group(x, y):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

