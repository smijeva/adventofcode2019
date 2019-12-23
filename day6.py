def orbit_count(file_name):
  file = open(file_name)
  orbits = {}
  for l in file.readlines():
    parts = l.split(")")
    center = parts[0].strip()
    orbit = parts[1].strip()
    if center in orbits:
      orbits[center].append(orbit)
    else:
      orbits[center] = [orbit]      
  file.close()

  count = 0
  queue = [("COM", 0)]
  while len(queue) > 0:
    current = queue.pop()
    center = current[0]
    distance = current[1] + 1
    if center not in orbits:
      continue
    for child in orbits[center]:
      count += distance
      queue.append((child, distance))

  return count

def main():
  c = orbit_count("input6.txt")
  print(c)

def test():
  t = orbit_count("input6test.txt")
  assert t == 42, f"t = {t}"
  print("ok")
