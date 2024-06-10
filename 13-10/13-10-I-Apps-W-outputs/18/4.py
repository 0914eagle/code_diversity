
def get_cafe_index(n, a):
    # Initialize a dictionary to store the last visit of each cafe
    last_visit = {}
    for i in range(n):
        # If the cafe is not in the dictionary, add it to the dictionary with the current index
        if a[i] not in last_visit:
            last_visit[a[i]] = i
        # If the cafe is already in the dictionary, update the last visit if the current index is greater than the stored last visit
        else:
            last_visit[a[i]] = max(last_visit[a[i]], i)
    
    # Find the cafe with the minimum last visit
    min_last_visit = min(last_visit.values())
    
    # Return the cafe with the minimum last visit
    return [cafe for cafe, visit in last_visit.items() if visit == min_last_visit][0]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_cafe_index(n, a))

if __name__ == '__main__':
    main()

