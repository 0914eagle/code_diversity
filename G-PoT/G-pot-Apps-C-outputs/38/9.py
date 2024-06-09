
# Read input
c, n, a = map(int, input().split())
accesses = [int(input()) for _ in range(a)]

# Initialize cache and dictionary to keep track of last access index
cache = []
last_access = {}

# Initialize variable to keep track of number of times an object must be read into cache
num_reads = 0

# Iterate through each access
for i, obj in enumerate(accesses):
    # If object is not in cache, add it and increment num_reads
    if obj not in cache:
        num_reads += 1
        # If cache is full, evict the object that will be accessed farthest in the future
        if len(cache) == c:
            farthest_access = max(last_access.values())
            obj_to_evict = None
            for key, value in last_access.items():
                if value == farthest_access:
                    obj_to_evict = key
                    break
            cache.remove(obj_to_evict)
            del last_access[obj_to_evict]
        cache.append(obj)
    
    # Update last access index for the object
    last_access[obj] = i

print(num_reads)
