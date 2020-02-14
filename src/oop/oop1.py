# Write classes for the following class hierarchy:
#
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

# BASE CLASS
class Vehicle:
    pass

# Inherit from Vehicle
class GroundVehicle(Vehicle):
    pass

# Inherit from GroundVehicle
class Car(GroundVehicle):
    pass

# Inherit from GroundVehicle
class Motorcycle(GroundVehicle):
    pass

# Inherit from Vehicle
class FlightVehicle(Vehicle):
    pass

# Inherit from FlightVehicle
class Airplane(FlightVehicle):
    pass

# Inherit from FlightVehicle
class Starship(FlightVehicle):
    pass