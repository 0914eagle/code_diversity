
def introspective_caching_algorithm(cache_size, num_objects, num_accesses, accesses):
    cache = set()
    cache_order = []
    cache_hits = 0

    for obj in accesses:
        if obj not in cache:
            if len(cache) == cache_size:
                next_accesses = accesses[accesses.index(obj):]
                next_accesses_set = set(next_accesses)
                objects_to_evict = cache.difference(next_accesses_set)
                if objects_to_evict:
                    evict_obj = max(objects_to_evict, key=lambda x: next_accesses.index(x))
                    cache.remove(evict_obj)
                    cache_order.remove(evict_obj)
            cache.add(obj)
            cache_order.append(obj)
        else:
            cache_order.remove(obj)
            cache_order.append(obj)
            cache_hits += 1

    return cache_hits

# Read input
cache_size, num_objects, num_accesses = map(int, input().split())
accesses = [int(input()) for _ in range(num_accesses)]

# Call the function and print the result
result = introspective_caching_algorithm(cache_size, num_objects, num_accesses, accesses)
print(result)
