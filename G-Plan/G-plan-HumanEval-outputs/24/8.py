
from typing import Tuple

def get_planets_between(planet1: str, planet2: str) -> Tuple[str, ...]:
    planets_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    
    if planet1 not in planets_order or planet2 not in planets_order:
        return ()
    
    start_idx = planets_order.index(planet1)
    end_idx = planets_order.index(planet2)
    
    if start_idx > end_idx:
        start_idx, end_idx = end_idx, start_idx
    
    result = []
    for i in range(start_idx + 1, end_idx):
        result.append(planets_order[i])
    
    return tuple(result)

planet1, planet2 = input().split()
result = get_planets_between(planet1, planet2)
print(result)
