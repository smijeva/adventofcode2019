param_combinations = []
for i in range(5,10):
  for j in range(5,10):
    for k in range(5,10):
      for l in range(5,10):
        for m in range(5,10):
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

class Computer:
  def __init__(self, numbers, inputs):
    self.numbers = numbers
    self.instr_pointer = 0
    self.inputs = inputs

  def execute(self, input):
    if input is not None:
      self.inputs.append(input)
    return self.compute(None)

  def compute(self, output):
    op_ix = self.instr_pointer
    opcode = self.numbers[op_ix]
    if opcode % 100 == 99:
      return None
    op = Operation(opcode, self.numbers[op_ix+1:op_ix+4], self.numbers)
    output = op.execute(self.numbers, self.inputs)
    self.instr_pointer = op.go_to if op.go_to != None else self.instr_pointer + op.shift
    if output != None:
      return output    
    return self.compute(output)


def compute_best(numbers):
  max_output = -10000000
  max_thrust = 0
  for comb in param_combinations:
    computers = []
    for i in range(5):
      computers.append(Computer(numbers.copy(), [comb[i]]))
    last_output = 0
    while True:
      for c in computers:
        last_output = c.execute(last_output)                      
      if last_output == None:
        if thrust > max_thrust:
            max_thrust = thrust
        break
      else:
        thrust = last_output
  return max_thrust

def main():
  file = open("input7.txt")
  line =  file.read()
  file.close()
  numbers = list(map(int, line.split(",")))
  best = compute_best(numbers)
  print(best)


def test():
  t_in = list(map(int, "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10".split(",")))
  t = compute_best(t_in)

  assert t == 18216, f"{t}"


  t_in = list(map(int, "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(",")))
  t = compute_best(t_in)

  assert t == 139629729, f"{t}"

  print("ok")
      