data = open("input.txt").readlines()
data = [int(x) for x in data]  # to convert into integers

def calc_fuel(mass):
    return int(mass)//3-2
# seperate the def function for calculations
total_fuel = 0
for mass in data:
    fuel_of_fuel = calc_fuel(mass)
    while fuel_of_fuel > 0:
        total_fuel = total_fuel + fuel_of_fuel
        fuel_of_fuel = calc_fuel(fuel_of_fuel)
print(total_fuel)
