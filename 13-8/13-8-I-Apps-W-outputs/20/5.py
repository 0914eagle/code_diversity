
def get_kth_digit(k):
    if k < 1:
        return -1
    
    count = 1
    num = 1
    while count < k:
        num += 1
        count += len(str(num))
    
    return str(num)[-k]

def main():
    k = int(input())
    print(get_kth_digit(k))

if __name__ == '__main__':
    main()

