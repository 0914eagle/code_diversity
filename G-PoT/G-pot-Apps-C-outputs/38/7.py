
def introspective_caching(cache_size, num_objects, num_accesses, accesses):
    cache = set()
    cache_order = []
    cache_counts = {}
    num_reads = 0
    
    for obj in accesses:
        if obj not in cache:
            num_reads += 1
            if len(cache) == cache_size:
                evict_obj = max(cache_order, key=lambda x: cache_counts.get(x, 0))
                cache.remove(evict_obj)
                cache_order.remove(evict_obj)
                del cache_counts[evict_obj]
            cache.add(obj)
            cache_order.append(obj)
        cache_counts[obj] = cache_counts.get(obj, 0) + 1
    
    return num_reads

# Read input
cache_size, num_objects, num_accesses = map(int, input().split())
accesses = [int(input()) for _ in range(num_accesses)]

# Call the function and output the result
result = introspective_caching(cache_size, num_objects, num_accesses, accesses)
print(result)
