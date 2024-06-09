
# Read input
c, n, a = map(int, input().split())
accesses = [int(input()) for _ in range(a)]

# Initialize cache and dictionary to keep track of last access index
cache = []
last_access = {}
num_reads = 0

# Iterate through each access
for i, obj in enumerate(accesses):
    # If object is not in cache, add it and increment num_reads
    if obj not in cache:
        num_reads += 1
        # If cache is full, evict the least recently accessed object
        if len(cache) == c:
            lra_obj = min(cache, key=lambda x: last_access.get(x, -1))
            cache.remove(lra_obj)
        cache.append(obj)
    # Update last access index of the object
    last_access[obj] = i

print(num_reads)
