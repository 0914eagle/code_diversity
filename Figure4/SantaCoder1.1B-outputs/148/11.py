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
    if planet1 == "mercury" or planet1 == "venus" or planet1 == "earth" or planet1 == "mars" or planet1 == "jupiter" or planet1 == "saturn" or planet1 == "uranus" or planet1 == "neptune":
        if planet2 == "mercury" or planet2 == "venus" or planet2 == "earth" or planet2 == "mars" or planet2 == "jupiter" or planet2 == "saturn" or planet2 == "uranus" or planet2 == "neptune":
            return ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        else:
            return ()
    else:
        return ()

