
def introspective_caching(cache_size, num_objects, num_accesses, accesses):
    cache = set()
    cache_order = []
    cache_counts = {}
    num_reads = 0

    for access in accesses:
        if access not in cache:
            num_reads += 1
            if len(cache) == cache_size:
                evict_object = max(cache_order, key=lambda x: cache_counts.get(x, 0))
                cache.remove(evict_object)
                cache_order.remove(evict_object)
                del cache_counts[evict_object]
            cache.add(access)
            cache_order.append(access)
        cache_counts[access] = cache_counts.get(access, 0) + 1

    return num_reads

# Read input
cache_size, num_objects, num_accesses = map(int, input().split())
accesses = [int(input()) for _ in range(num_accesses)]

# Call the function and print the result
result = introspective_caching(cache_size, num_objects, num_accesses, accesses)
print(result)
