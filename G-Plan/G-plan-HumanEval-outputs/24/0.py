
from typing import Tuple

def get_ordered_planets() -> Tuple[str, ...]:
    return ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    planets = get_ordered_planets()
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    start_idx = planets.index(planet1)
    end_idx = planets.index(planet2)
    
    if start_idx > end_idx:
        start_idx, end_idx = end_idx, start_idx
    
    result = planets[start_idx+1:end_idx]
    
    return tuple(result)

# Test the function with the provided examples
print(bf('Jupiter', 'Neptune'))
print(bf('Earth', 'Mercury'))
print(bf('Mercury', 'Uranus'))
