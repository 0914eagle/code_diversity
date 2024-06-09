
def introspective_caching_algorithm(cache_size, num_objects, num_accesses, accesses):
    cache = set()
    cache_order = []
    cache_reads = 0
    
    for obj in accesses:
        if obj not in cache:
            cache_reads += 1
            if len(cache) == cache_size:
                evict_obj = cache_order.pop(0)
                cache.remove(evict_obj)
        else:
            cache_order.remove(obj)
        
        cache.add(obj)
        cache_order.append(obj)
    
    return cache_reads

# Read input
cache_size, num_objects, num_accesses = map(int, input().split())
accesses = [int(input()) for _ in range(num_accesses)]

# Call the function and output the result
result = introspective_caching_algorithm(cache_size, num_objects, num_accesses, accesses)
print(result)
