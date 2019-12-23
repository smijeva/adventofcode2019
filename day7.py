param_combinations = []
for i in range(5):
  for j in range(5):
    for k in range(5):
      for l in range(5):
        for m in range(5):
          combination = [i,j,k,l,m]
          if len(set(combination)) != 5:
            continue
          param_combinations.append(combination)

class Operation:
  def get_param(self, par_mode, i, opcode, successors, numbers):
    if par_mode == 0:
      par_ix = successors[i]
      return numbers[par_ix]
    else:
      return successors[i]

  def __init__(self, opcode, successors, numbers):
    self.go_to = None
    opcodecpy = opcode
    self.code = opcode % 100
    opcode = opcode // 100
    if self.code == 1 or self.code == 2 or self.code == 7 or self.code == 8:
      self.shift = 4
      par_mode = opcode % 10
      opcode = opcode // 10
      self.p1 = self.get_param(par_mode, 0, opcode, successors, numbers)
      par_mode = opcode % 10
      self.p2 = self.get_param(par_mode, 1, opcode, successors, numbers)
      self.output = successors[2]
    elif self.code == 3 or self.code == 4:
      self.shift = 2
      self.output = successors[0]
    elif self.code == 5 or self.code == 6:
      self.shift = 3
      par_mode = opcode % 10
      opcode = opcode // 10
      self.p1 = self.get_param(par_mode, 0, opcode, successors, numbers)
      par_mode = opcode % 10
      self.p2 = self.get_param(par_mode, 1, opcode, successors, numbers)
    else:
      print(opcodecpy)
      print("Something terrible happened :(")

  def execute(self, numbers, inputs):
    if self.code == 1:
      numbers[self.output] = self.p1 + self.p2
    elif self.code == 2:
      numbers[self.output] = self.p1 * self.p2
    elif self.code == 3:
      numbers[self.output] = inputs.pop(0)
    elif self.code == 4:      
      return numbers[self.output]
    elif self.code == 5:
      if self.p1 != 0:
        self.go_to = self.p2
    elif self.code == 6:
      if self.p1 == 0:
        self.go_to = self.p2
    elif self.code == 7:      
      numbers[self.output] = 1 if self.p1 < self.p2 else 0
    elif self.code == 8:
      numbers[self.output] = 1 if self.p1 == self.p2 else 0


def compute_best(numbers):
  max_output = -10000000
  for c in param_combinations:
    input = 0
    for i in c:
      numbers_cpy = numbers.copy()
      output = compute(numbers_cpy, [i, input], 0, None)
      input = output
    if output > max_output:
      max_output = output
  return max_output

def compute(numbers, inputs, zero_ix, output):
  op_ix = zero_ix
  opcode = numbers[op_ix]
  if opcode % 100 == 99:
    return output

  op = Operation(opcode, numbers[op_ix+1:op_ix+4], numbers)
  output = op.execute(numbers, inputs)
  new_zero = op.go_to if op.go_to != None else zero_ix + op.shift
  return compute(numbers, inputs, new_zero, output)

def main():
  file = open("input7.txt")
  line =  file.read()
  file.close()
  numbers = list(map(int, line.split(",")))
  best = compute_best(numbers)
  print(best)


def test():
  t_in = list(map(int, "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(",")))
  t = compute_best(t_in)

  assert t == 43210, f"{t}"

  t_in = list(map(int, "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(",")))
  t = compute_best(t_in)

  assert t == 54321, f"{t}"

  t_in = list(map(int, "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(",")))
  t = compute_best(t_in)

  assert t == 65210, f"{t}"

  print("ok")
      