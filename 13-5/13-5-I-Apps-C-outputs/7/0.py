
def is_winnable(a):
    # Check if all piles are empty
    if all(a == 0):
        return False
    
    # Check if there are two piles with the same number of stones
    if len(set(a)) == 1:
        return False
    
    # Check if Tokitsukaze can make a valid move
    for i in range(len(a)):
        if a[i] > 0:
            return True
    
    # If Tokitsukaze cannot make a valid move, CSL will win
    return False

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if is_winnable(a):
        print("sjfnb")
    else:
        print("cslnb")

if __name__ == '__main__':
    main()

