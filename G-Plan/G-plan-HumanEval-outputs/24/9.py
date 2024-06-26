
from typing import Tuple

def get_planets_between(planet1: str, planet2: str) -> Tuple[str, ...]:
    planets_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets_order or planet2 not in planets_order:
        return ()
    
    start_index = planets_order.index(planet1)
    end_index = planets_order.index(planet2)
    
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    
    return tuple(planet for planet in planets_order[start_index+1:end_index] if planet != planet1 and planet != planet2)

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    planets_between = get_planets_between(planet1, planet2)
    return planets_between

planet1, planet2 = input().split()
print(bf(planet1, planet2))
