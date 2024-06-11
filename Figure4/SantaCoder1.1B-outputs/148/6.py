def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planet1 = planet1.lower()
    planet2 = planet2.lower()
    if planet1 not in planets or planet2 not in planets:
        return ()
    if planet1 == "mercury":
        return ("venus", "earth", "mars", "jupiter", "saturn")
    if planet1 == "venus":
        return ("earth", "mars", "jupiter", "saturn")
    if planet1 == "earth":
        return ("mercury", "venus", "mars", "jupiter", "saturn")
    if planet1 == "mars":
        return ("venus", "earth", "jupiter", "saturn")
    if planet1 == "jupiter":
        return ("earth", "mars", "saturn")
    if planet1 == "saturn":
        return ("earth", "mars", "jupiter")
    if planet1 == "uranus":
        return ("earth", "mars", "jupiter", "saturn")
    if planet1 == "neptune":
        return ("earth", "mars", "jupiter", "saturn", "uranus")
    return ()

