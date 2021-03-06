def mass_to_fuel(mass):
  fuel_for_mass = (mass // 3) - 2
  if fuel_for_mass < 0:
    return 0
  return fuel_for_mass + mass_to_fuel(fuel_for_mass)


def main():
  file = open("input1.txt")
  fuel_sum = 0
  for line in file:
    fuel_sum += mass_to_fuel(int(line))
  print(fuel_sum)
  file.close()


def test():
  t1 = mass_to_fuel(12)
  assert t1 == 2, f"t1 = {t1}"

  t2 = mass_to_fuel(14)
  assert t2 == 2, f"t2 = {t2}"

  t3 = mass_to_fuel(1969)
  assert t3 == 966, f"t3 = {t3}"

  t4 = mass_to_fuel(100756)
  assert t4 == 50346, f"t4 = {t4}"

  print("ok")


