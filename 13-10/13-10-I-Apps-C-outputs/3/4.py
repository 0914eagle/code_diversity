
def get_chaos(passengers, order):
    
    total_chaos = 0
    for i in order:
        total_chaos += passengers[i - 1]
        passengers[i - 1] = 0
    return total_chaos

def main():
    n = int(input())
    passengers = list(map(int, input().split()))
    order = list(map(int, input().split()))
    print(get_chaos(passengers, order))

if __name__ == '__main__':
    main()

