import math


def fuel_for_mass(module_mass):
    return math.floor(module_mass / 3) - 2


def fuel_for_mass_rec(mass):
    if mass <= 0:
        return 0
    fuel = math.floor(mass / 3) - 2
    fuel_for_fuel = fuel_for_mass_rec(fuel)
    if fuel_for_fuel > 0:
        return fuel + fuel_for_fuel
    else:
        return fuel


lines = [int(line) for line in open('input.txt')]

print(fuel_for_mass(1969) + fuel_for_mass(654) + fuel_for_mass(216) + fuel_for_mass(70) + fuel_for_mass(21) + fuel_for_mass(5))
print(fuel_for_mass_rec(1969))
print(sum(list(map(fuel_for_mass_rec, lines))))

