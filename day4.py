range1 = 245182
range2 = 790572

def is_valid_pass(number_str):
  last_number = -1
  has_double = False
  for c in number_str:
    current = int(c)
    if current < last_number:
      return False
    if current == last_number:
      has_double = True
    last_number = current
  return has_double

def main():
  valid_count = 0
  for i in range(range1, range2+1):
    if is_valid_pass(str(i)):
      valid_count += 1
  print(valid_count)


def test():
  t1 = is_valid_pass("111111")
  assert t1 is True, "111111 is False"

  t2 = is_valid_pass("223450")
  assert t2 is False, "223450 is True"

  t3 = is_valid_pass("123789")
  assert t3 is False, "123789 is True"

  print("ok")
