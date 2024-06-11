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
    if planet1 in planets and planet2 in planets:
        if planet1 == "mercury":
            planet1 = "mercury"
        if planet2 == "mercury":
            planet2 = "mercury"
        if planet1 == "venus":
            planet1 = "venus"
        if planet2 == "venus":
            planet2 = "venus"
        if planet1 == "earth":
            planet1 = "earth"
        if planet2 == "earth":
            planet2 = "earth"
        if planet1 == "mars":
            planet1 = "mars"
        if planet2 == "mars":
            planet2 = "mars"
        if planet1 == "jupiter":
            planet1 = "jupiter"
        if planet2 == "jupiter":
            planet2 = "jupiter"
        if planet1 == "saturn":
            planet1 = "saturn"
        if planet2 == "saturn":
            planet2 = "saturn"
        if planet1 == "uranus":
            planet1 = "uranus"
        if planet2 == "uranus":
            planet2 = "uranus"
        if planet1 == "neptune":
            planet1 = "neptune"
        if planet2 == "neptune":
            planet2 = "neptune"
        return (planet1, planet2)
    else:
        return ()

