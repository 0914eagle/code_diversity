
def get_price_list(n):
    return list(map(int, input().split()))

def get_threshold(n):
    return int(input())

def get_consecutive_subsequences(price_list, threshold):
    subsequences = []
    for i in range(len(price_list)):
        for j in range(i+1, len(price_list)+1):
            if sum(price_list[i:j])/j >= threshold:
                subsequences.append(price_list[i:j])
    return len(set(map(tuple, subsequences)))

def main():
    n = int(input())
    price_list = get_price_list(n)
    threshold = get_threshold(n)
    print(get_consecutive_subsequences(price_list, threshold))

if __name__ == '__main__':
    main()

