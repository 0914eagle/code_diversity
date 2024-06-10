
def check_mod_k(k, c_list):
    # Check if k is in the list of ancient numbers
    if k in c_list:
        return True
    
    # Check if any of the ancient numbers is a factor of k
    for c in c_list:
        if k % c == 0:
            return True
    
    # If k is not a factor of any of the ancient numbers, then Arya cannot determine the value of x mod k
    return False

def check_mod_ancient(k, x, c_list):
    # Check if k is in the list of ancient numbers
    if k in c_list:
        return x % k
    
    # Check if any of the ancient numbers is a factor of k
    for c in c_list:
        if k % c == 0:
            return x % c
    
    # If k is not a factor of any of the ancient numbers, then Arya cannot determine the value of x mod k
    return None

def main():
    n, k = map(int, input().split())
    c_list = list(map(int, input().split()))
    
    if check_mod_k(k, c_list):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

