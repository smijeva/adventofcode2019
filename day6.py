def make_orbits(file_name):
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
  return orbits

def make_reverse_orbits(file_name):
  file = open(file_name)
  reverse_orbits = {}
  for l in file.readlines():
    parts = l.split(")")
    center = parts[0].strip()
    orbit = parts[1].strip()
    reverse_orbits[orbit] = center    
  file.close()
  return reverse_orbits

def orbit_count(file_name): 
  orbits = make_orbits(file_name)
  count = 0
  stack = [("COM", 0)]
  while len(stack) > 0:
    current = stack.pop()
    center = current[0]
    distance = current[1] + 1
    if center not in orbits:
      continue
    for child in orbits[center]:
      count += distance
      stack.append((child, distance))
  return count

def get_path(reverse_orbits, object_name):
  path = [object_name]
  while (path[-1] != "COM"):
    current = path[-1]
    predecessor = reverse_orbits[current]
    path.append(predecessor)
  return path

def shortest_path(file_name):
  reverse_orbits = make_reverse_orbits(file_name)
  santa_path = get_path(reverse_orbits, "SAN")
  you_path = get_path(reverse_orbits, "YOU")
  while santa_path[-1] == you_path[-1]:
    santa_path.pop()
    you_path.pop()
  dist = len(santa_path) + len(you_path) - 2
  return 0 if dist < 0 else dist

def main():
  c = shortest_path("input6.txt")
  print(c)

def test():
  t = orbit_count("input6test.txt")
  assert t == 42, f"t = {t}"

  t = shortest_path("input6test2.txt")
  assert t == 4, f"t = {t}"
  print("ok")
