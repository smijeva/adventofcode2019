class Operation:
  def get_param(self, par_mode, i, opcode, successors, numbers):
    if par_mode == 0:
      par_ix = successors[i]
      return numbers[par_ix]
    else:
      return successors[i]

  def __init__(self, opcode, successors, numbers):
    self.code = opcode % 100
    self.go_to = None
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
      print(opcode)
      print("Something terrible happened :(")

  def execute(self, numbers):
    if self.code == 1:
      #print(f"#1 numbers[{self.output}] = {self.p1} + {self.p2}")
      numbers[self.output] = self.p1 + self.p2
    elif self.code == 2:
      #print(f"#1 numbers[{self.output}] = {self.p1} * {self.p2}")
      numbers[self.output] = self.p1 * self.p2
    elif self.code == 3:
      x = input("Input for instruction #3: ")
      numbers[self.output] = int(x)
    elif self.code == 4:      
      print(f"#4 numbers[{self.output}] is {numbers[self.output]}")
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


def compute(numbers, zero_ix, output):
  op_ix = zero_ix
  opcode = numbers[op_ix]
  if opcode % 100 == 99:
    return output

  op = Operation(opcode, numbers[op_ix+1:op_ix+4], numbers)
  op.execute(numbers)
  new_zero = op.go_to if op.go_to != None else zero_ix + op.shift
  
  output = compute(numbers, new_zero, output)

def main():
  file = open("input5.txt")
  line =  file.read()
  file.close()
  numbers = list(map(int, line.split(",")))
  compute(numbers, 0, None)

def test():
  t1_in = list(map(int, "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(",")))
  t1 = compute(t1_in, 0, None)

  assert t1 == 999
      