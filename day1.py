def mass_to_fuel(mass):
  mass_int = int(mass)
  return (mass_int // 3) - 2


def main():
  file = open("input1.txt")
  fuel_sum = 0
  for line in file:
    fuel_sum += mass_to_fuel(line)
  print(fuel_sum)
  file.close()


def test():
  t1 = mass_to_fuel(12)
  assert t1 == 2, f"t1 = {t1}"

  t2 = mass_to_fuel(14)
  assert t2 == 2, f"t2 = {t2}"

  t3 = mass_to_fuel(1969)
  assert t3 == 654, f"t3 = {t3}"

  t4 = mass_to_fuel(100756)
  assert t4 == 33583, f"t4 = {t4}"

  print("ok")


