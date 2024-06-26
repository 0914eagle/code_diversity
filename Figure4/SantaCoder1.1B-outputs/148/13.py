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
    if planet1 == "mercury" and planet2 == "venus":
        return ("Venus",)
    if planet1 == "venus" and planet2 == "earth":
        return ("Earth",)
    if planet1 == "earth" and planet2 == "mars":
        return ("Mars",)
    if planet1 == "mars" and planet2 == "jupiter":
        return ("Jupiter",)
    if planet1 == "jupiter" and planet2 == "saturn":
        return ("Saturn",)
    if planet1 == "saturn" and planet2 == "uranus":
        return ("Uranus",)
    if planet1 == "uranus" and planet2 == "neptune":
        return ("Neptune",)
    return ()

