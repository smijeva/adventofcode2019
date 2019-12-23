class Operation:
  def get_param(self, par_mode, i, opcode, successors, numbers):
    if par_mode == 0:
      par_ix = successors[i]
      return numbers[par_ix]
    else:
      return successors[i]

  def __init__(self, opcode, successors, numbers):
    self.code = opcode % 100
    opcode = opcode // 100
    if self.code == 1 or self.code == 2:
      self.shift = 4
      par_mode = opcode % 10
      opcode = opcode // 10
      p1 = self.get_param(par_mode, 0, opcode, successors, numbers)
      par_mode = opcode % 10
      p2 = self.get_param(par_mode, 1, opcode, successors, numbers)
      self.output = successors[2]
      self.params = [p1, p2]
    elif self.code == 3 or self.code == 4:
      self.shift = 2
      self.output = successors[0]
    else:
      print(opcode)
      print("Something terrible happened :(")

  def execute(self, numbers):
    if self.code == 1:
      print(f"#1 numbers[{self.output}] = {self.params[0]} + {self.params[1]}")
      numbers[self.output] = self.params[0] + self.params[1]
    elif self.code == 2:
      print(f"#2 numbers[{self.output}] = {self.params[0]} * {self.params[1]}")
      numbers[self.output] = self.params[0] * self.params[1]
    elif self.code == 3:
      x = input("Input for instruction #3: ")
      numbers[self.output] = int(x)
    elif self.code == 4:      
      print(f"#4 numbers[{self.output}] is {numbers[self.output]}")


def compute(numbers, zero_ix):
  op_ix = zero_ix
  opcode = numbers[op_ix]
  if opcode % 100 == 99:
    return

  op = Operation(opcode, numbers[op_ix+1:op_ix+4], numbers)
  op.execute(numbers)
  new_zero = zero_ix + op.shift
  
  compute(numbers, new_zero)

def main():
  file = open("input5.txt")
  line =  file.read()
  file.close()
  numbers = list(map(int, line.split(",")))
  compute(numbers, 0)
      