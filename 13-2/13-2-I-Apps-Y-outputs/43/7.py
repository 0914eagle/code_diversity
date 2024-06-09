
def count_pairs(k):
    count = 0
    for i in range(1, k+1, 2):
        for j in range(2, k+1, 2):
            count += 1
    return count

def main():
    k = int(input())
    print(count_pairs(k))

if __name__ == '__main__':
    main()

