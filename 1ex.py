#First we'll need a class to represent the solar system. Let's call it System, and give it an attribute bodies. bodies will start as an empty list (ie. []).
class System:
   
   def __init__(self, bodies):
    self.bodies = []

#instance method add
    def add(self, celestial_body):
#add a celestial body to the list. 
        self.bodies.append(celestial_body)

#instance method total_mass
    def total_mass(self):
        total = 0 #start of the loop
        # add up the mass of all the bodies in bodies,
        for body in self.bodies:
            total += body.mass
            # and return it.
        return total

#class Body. 
class Body(System):
#name and a mass. 
#We'll assign them when we create the body.
    self.name = name
    self.mass = mass

class Planet(Body):
#they all have a name and a mass. 
    def __init__(self, name, mass, )

#let's also make them inherit from Body
    super().__init__(name, mass)
        self.day = day
        self.year = year

#Have a type (ie. our Sun is a G-type star) + name, + mass
class Star(Body):

    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

class Moon(Body):
    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.planet = planet   
        self.month = month



milky_way = System()
pluto = Body()
pluto.mass = 1000
milky_way.add(pluto)
milky_way.total_mass

print(System().bodies)
print((System).total_mass)
