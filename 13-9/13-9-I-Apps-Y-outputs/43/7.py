
def is_reachable(districts, gangs, current_district, visited):
    if current_district == len(districts):
        return True
    
    visited.add(current_district)
    for next_district in range(len(districts)):
        if next_district not in visited and gangs[current_district] != gangs[next_district]:
            if is_reachable(districts, gangs, next_district, visited):
                return True
    return False

def can_build_roads(districts, gangs):
    roads = []
    for i in range(len(districts)):
        for j in range(i+1, len(districts)):
            if gangs[i] != gangs[j]:
                roads.append((i+1, j+1))
    return roads

def solve(districts, gangs):
    roads = can_build_roads(districts, gangs)
    if len(roads) < len(districts) - 1:
        return "NO"
    
    visited = set()
    for road in roads:
        if not is_reachable(districts, gangs, road[0]-1, visited):
            return "NO"
        if not is_reachable(districts, gangs, road[1]-1, visited):
            return "NO"
    
    return "YES\n" + "\n".join([f"{i} {j}" for i, j in roads])

if __name__ == '__main__':
    num_cases = int(input())
    for case in range(1, num_cases+1):
        num_districts = int(input())
        gangs = [int(x) for x in input().split()]
        print(f"Case {case}: {solve(num_districts, gangs)}")

