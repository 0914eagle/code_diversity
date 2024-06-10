
from typing import Tuple

def get_planets_between(planet1: str, planet2: str) -> Tuple[str, ...]:
    planets_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    
    if planet1 not in planets_order or planet2 not in planets_order:
        return ()
    
    start_idx = planets_order.index(planet1)
    end_idx = planets_order.index(planet2)
    
    if start_idx > end_idx:
        start_idx, end_idx = end_idx, start_idx
    
    result = tuple(planet for planet in planets_order[start_idx+1:end_idx] if planet != planet1 and planet != planet2)
    
    return result

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    planets_between = get_planets_between(planet1, planet2)
    return planets_between

planet1, planet2 = input().split()
result = bf(planet1, planet2)
print(result)
