
from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index
    return tuple(planets[planet1_index+1:planet2_index])

