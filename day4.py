range1 = 245182
range2 = 790572

def is_valid_pass(number_str):
  last_number = -1
  has_double = False
  numbers = list(map(lambda i: int(i), list(number_str)))
  for i in range(len(numbers)):
    current = numbers[i]
    if current < last_number:
      return False
    if current == last_number:
      if look_ahead(numbers, i) and look_behind(numbers, i):
        has_double = True      
    last_number = current
  return has_double

def look_ahead(numbers, i):
  ahead = i + 1
  if ahead >= len(numbers):
    return True
  return numbers[ahead] != numbers[i]

def look_behind(numbers, i):
  behind = i - 2
  if behind < 0:
    return True
  return numbers[behind] != numbers[i]

def main():
  valid_count = 0
  for i in range(range1, range2+1):
    if is_valid_pass(str(i)):
      valid_count += 1
  print(valid_count)


def test():
  t1 = is_valid_pass("112233")
  assert t1 is True, "112233 is False, True expected"

  t2 = is_valid_pass("123444")
  assert t2 is False, "123444 is True, False expected"

  t3 = is_valid_pass("111122")
  assert t3 is True, "111122 is False, True expected"

  print("ok")
