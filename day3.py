def go(path, direction):
  last_coor = path[-1].copy()

  azimuth = direction[0]
  dir_ix = 0 if azimuth == "L" or azimuth == "R" else 1
  dir_step = 1 if azimuth == "R" or azimuth == "U" else -1  

  step_count = int(direction[1:])
  for i in range(step_count):
    last_coor[dir_ix] += dir_step
    path.append(last_coor.copy())


def make_path(directions):
  path = [ [0, 0] ]
  for d in directions:
    go(path, d)
  return path


def intersection(directions1, directions2):
  path1 = make_path(directions1)[1:]
  path2 = make_path(directions2)[1:]
  hashed_path2 = [str(x) for x in path2]
  intersections = [value for value in path1 if str(value) in hashed_path2]
  min_dist = abs(intersections[0][0]) + abs(intersections [0][1])
  for i in range(len(intersections)):
    dist = abs(intersections[i][0]) + abs(intersections [i][1])
    if dist < min_dist:
      min_dist = dist
  return min_dist

def main():
  file = open("input3.txt")
  line1 = file.readline()
  line2 = file.readline()
  file.close()
  directions1 = line1.split(",")
  directions2 = line2.split(",")

  print(intersection(directions1, directions2))
  
def test():
  t1 = make_path(["U3","R2","D1","L2"])

  assert t1 == [[0,0],[0,1],[0,2],[0,3],[1,3],[2,3],[2,2],[1,2],[0,2]], f"t1 = {t1}"

  t2_p1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
  t2_p2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")
  t2 = intersection(t2_p1, t2_p2)

  assert t2 == 159, f"t2 = {t2}"

  t3_p1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
  t3_p2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")
  t3 = intersection(t3_p1, t3_p2)

  assert t3 == 135, f"t3 = {t3}"

  print("ok")
