with open('input.txt', 'r' ) as data:
    mass =  [int(line.strip())for line in data]



def math(mass):
  total_fuel = 0
  for i in mass:
    calculated = i // 3 - 2
    total_fuel += calculated
  return total_fuel


print(math(mass))
