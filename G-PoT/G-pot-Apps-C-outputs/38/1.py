
def introspective_caching_algorithm(cache_size, num_objects, num_accesses, accesses):
    cache = []
    cache_dict = {}
    cache_hits = 0

    for obj in accesses:
        if obj in cache_dict:
            cache_hits += 1
            cache.remove(obj)
            cache.append(obj)
        else:
            if len(cache) == cache_size:
                evict_obj = cache.pop(0)
                del cache_dict[evict_obj]
            cache.append(obj)
            cache_dict[obj] = True

    return num_accesses - cache_hits

# Read input
cache_size, num_objects, num_accesses = map(int, input().split())
accesses = [int(input()) for _ in range(num_accesses)]

# Call the function and print the result
result = introspective_caching_algorithm(cache_size, num_objects, num_accesses, accesses)
print(result)
