
def introspective_caching_algorithm(cache_size, num_objects, num_accesses, accesses):
    cache = set()
    cache_order = []
    cache_hits = 0

    for obj in accesses:
        if obj in cache:
            cache_order.remove(obj)
            cache_order.append(obj)
            cache_hits += 1
        else:
            if len(cache) < cache_size:
                cache.add(obj)
                cache_order.append(obj)
            else:
                evicted_obj = cache_order.pop(0)
                cache.remove(evicted_obj)
                cache.add(obj)
                cache_order.append(obj)

    return cache_hits

# Read input
cache_size, num_objects, num_accesses = map(int, input().split())
accesses = [int(input()) for _ in range(num_accesses)]

# Call the function and output the result
result = introspective_caching_algorithm(cache_size, num_objects, num_accesses, accesses)
print(result)
