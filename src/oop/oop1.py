# Write classes for the following class hierarchy:
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# setting up main class here
class Vehicle:
  def __init__(self, name, typeOfVehicle):
    
    self.name = name
    self.typeOfVehicle = typeOfVehicle
    
    
  def whatVehicle(self):
    return f'{self.name} is a {self.typeOfVehicle}'
    

car = Vehicle('Car', 'GroundVehicle')
print(car.whatVehicle())

motorcycle = Vehicle('Motorcycle', 'GroundVehicle')
print(motorcycle.whatVehicle())

airplane = Vehicle('Airplane', 'FlightVehicle')
print(airplane.whatVehicle())

starship = Vehicle('Starship', 'FlightVehicle i think :)')
print(starship.whatVehicle())