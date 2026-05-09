class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        elif not name or not planet_type or not star:
            raise ValueError('name, planet_type, and star must be non-empty strings')

        self.name = name
        self.planet_type = planet_type
        self.star = star
    
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


planet_1 = Planet('Earth', 'Terrestrial', 'Sun')
planet_2 = Planet('Proxima Centauri b', 'Terrestrial/Super-Earth', 'Proxima Centauri')
planet_3 = Planet('Jupiter', 'Gas Giant', 'Sun')
planet_4 = Planet('Kepler-22b', 'Terrestrial/Super-Earth', 'Kepler-22')
planet_5 = Planet('TRAPPIST-1e', 'Terrestrial', 'TRAPPIST-1')
planet_6 = Planet('Neptune', 'Ice Giant', 'Sun')
planet_7 = Planet('Saturn', 'Gas Giant', 'Sun')

print(planet_1)
print(planet_2)
print(planet_3)
print(planet_4)
print(planet_5)
print(planet_6)
print(planet_7, end='\n\n')

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
print(planet_4.orbit())
print(planet_5.orbit())
print(planet_6.orbit())
print(planet_7.orbit())