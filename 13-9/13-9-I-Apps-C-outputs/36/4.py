
def find_mod(k, c_list):
    # Check if k is in the list of ancient numbers
    if k in c_list:
        return "Yes"
    
    # Check if any of the ancient numbers is a factor of k
    for c in c_list:
        if k % c == 0:
            return "Yes"
    
    # If none of the above conditions are met, then Arya cannot determine the value of x mod k
    return "No"

def main():
    n, k = map(int, input().split())
    c_list = list(map(int, input().split()))
    print(find_mod(k, c_list))

if __name__ == '__main__':
    main()

