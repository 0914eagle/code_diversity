
from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    if planet1_index > planet2_index:
        return tuple(reversed(planets[planet2_index+1:planet1_index]))
    else:
        return tuple(planets[planet1_index+1:planet2_index])

