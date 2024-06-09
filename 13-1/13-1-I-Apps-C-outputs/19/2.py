
def f1(c, n, a):
    # Initialize a dictionary to store the number of times each object is accessed
    access_count = {}
    for i in range(n):
        access_count[i] = 0
    
    # Iterate through the accesses and increment the count for each object accessed
    for i in range(a):
        obj = int(input())
        access_count[obj] += 1
    
    # Sort the access count in descending order
    access_count = sorted(access_count.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize a variable to store the number of times an object must be read into the cache
    cache_hits = 0
    
    # Iterate through the access count and calculate the number of times an object must be read into the cache
    for obj, count in access_count:
        if count > 0:
            cache_hits += 1
    
    return cache_hits

def f2(c, n, a):
    # Initialize a dictionary to store the number of times each object is accessed
    access_count = {}
    for i in range(n):
        access_count[i] = 0
    
    # Iterate through the accesses and increment the count for each object accessed
    for i in range(a):
        obj = int(input())
        access_count[obj] += 1
    
    # Sort the access count in descending order
    access_count = sorted(access_count.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize a variable to store the number of times an object must be read into the cache
    cache_hits = 0
    
    # Iterate through the access count and calculate the number of times an object must be read into the cache
    for obj, count in access_count:
        if count > 0:
            cache_hits += 1
    
    return cache_hits

if __name__ == '__main__':
    c, n, a = map(int, input().split())
    print(f1(c, n, a))
    print(f2(c, n, a))

