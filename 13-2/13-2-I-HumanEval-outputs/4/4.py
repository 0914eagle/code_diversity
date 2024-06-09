
from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    if idx1 < idx2:
        return tuple(planets[idx1+1:idx2])
    else:
        return tuple(planets[idx2+1:idx1])
