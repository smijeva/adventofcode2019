relative_base = 0

class Operation:
  def get_param(self, par_mode, i, successors, numbers):
    global relative_base
    if par_mode == 0:
      par_ix = successors[i]
      return numbers[par_ix]
    elif par_mode == 1:
      return successors[i]
    else:
      par_ix = successors[i] + relative_base
      return numbers[par_ix]
  
  def get_output(self, par_mode, i, successors, numbers):
    global relative_base
    if par_mode == 0:
      return successors[i]
    elif par_mode == 2:
      par_ix = successors[i] + relative_base
      return par_ix
    else:
      print("Weird output mode: " + str(par_mode))

  def __init__(self, opcode, successors, numbers):
    self.code = opcode % 100
    self.go_to = None
    opcode = opcode // 100
    if self.code == 1 or self.code == 2 or self.code == 7 or self.code == 8:
      self.shift = 4
      par_mode = opcode % 10
      opcode = opcode // 10
      self.p1 = self.get_param(par_mode, 0, successors, numbers)
      par_mode = opcode % 10
      opcode = opcode // 10
      self.p2 = self.get_param(par_mode, 1, successors, numbers)
      par_mode = opcode % 10
      self.output = self.get_output(par_mode, 2, successors, numbers)
    elif self.code == 3:
      self.shift = 2
      par_mode = opcode % 10
      self.output = self.get_output(par_mode, 0, successors, numbers)
    elif self.code == 4:
      self.shift = 2
      par_mode = opcode % 10
      self.p1 = self.get_param(par_mode, 0, successors, numbers)
    elif self.code == 5 or self.code == 6:
      self.shift = 3
      par_mode = opcode % 10
      opcode = opcode // 10
      self.p1 = self.get_param(par_mode, 0, successors, numbers)
      par_mode = opcode % 10
      self.p2 = self.get_param(par_mode, 1, successors, numbers)
    elif self.code == 9:
      self.shift = 2
      par_mode = opcode % 10
      self.p1 = self.get_param(par_mode, 0, successors, numbers)      
    else:
      print("Something terrible happened :(... operation code was: " + self.code)

  def execute(self, numbers):
    if self.code == 1:
      numbers[self.output] = self.p1 + self.p2
    elif self.code == 2:
      numbers[self.output] = self.p1 * self.p2
    elif self.code == 3:
      x = input("Input for instruction #3: ")
      numbers[self.output] = int(x)
    elif self.code == 4:  
      print(f"output: {self.p1}")
      return self.p1
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
    elif self.code == 9:
      global relative_base
      relative_base += self.p1
      

def compute(numbers):
  numbers_count = len(numbers) * 10
  numbers = numbers + [0 for i in range(numbers_count)]
  op_ix = 0

  while True:
    opcode = numbers[op_ix]
    if opcode % 100 == 99:
      return

    op = Operation(opcode, numbers[op_ix+1:op_ix+4], numbers)
    op.execute(numbers)
    op_ix = op.go_to if op.go_to != None else op_ix + op.shift

def main():
  file = open("input9.txt")
  line =  file.read()
  file.close()
  numbers = list(map(int, line.split(",")))
  
  compute(numbers)
      
def test():
  print("#1")
  t_in = list(map(int, "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(",")))
  compute(t_in)

  print("#2")
  t_in = list(map(int, "1102,34915192,34915192,7,4,7,99,0".split(",")))
  compute_(t_in)

  print("#3")
  t_in = list(map(int, "104,1125899906842624,99".split(",")))
  compute_(t_in)