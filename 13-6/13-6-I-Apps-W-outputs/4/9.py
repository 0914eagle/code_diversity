
def add_to_set(x):
    # add x to the set, if it's not already in the set
    if x not in set:
        set.add(x)

def find_subset():
    # find the subset with the maximum possible value of max(s) - mean(s)
    # return the maximum possible value
    pass

def main():
    set = set()
    queries = int(input())
    for i in range(queries):
        query = input().split()
        if query[0] == "1":
            add_to_set(int(query[1]))
        elif query[0] == "2":
            print(find_subset())

if __name__ == '__main__':
    main()

