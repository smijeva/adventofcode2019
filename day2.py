def compute(numbers, zero):
  op_ix = zero
  opcode = numbers[op_ix]
  if opcode == 99:
    return

  if opcode != 1 and opcode != 2:
    print("smth terrible happened :(")
    return

  in1_ix = zero + 1
  in2_ix = zero + 2
  out_ix = zero + 3
  new_zero = zero + 4

  input1_ix = numbers[in1_ix]
  input2_ix = numbers[in2_ix]
  output_ix = numbers[out_ix]
  
  input1 = numbers[input1_ix]
  input2 = numbers[input2_ix]
  
  output = input1 + input2 if (opcode == 1) else input1 * input2
  numbers[output_ix] = output
  compute(numbers, new_zero)

def main():
  file = open("input2.txt")
  line =  file.read()
  file.close()
  numbers = list(map(int, line.split(",")))
  for i in range(100):
    for j in range(100):
      attempt = numbers.copy()
      attempt[1] = i
      attempt[2] = j
      compute(attempt, 0)
      if attempt[0] == 19690720:
        print(i)
        print(j)


def test():
  t1 = [1, 0, 0, 0, 99]
  compute(t1, 0)

  assert t1 == [2, 0, 0, 0, 99], f"t1 = {t1}"

  t2 = [2,3,0,3,99]
  compute(t2, 0)

  assert t2 == [2,3,0,6,99], f"t2 {t2}"

  t3 = [2,4,4,5,99,0]
  compute(t3, 0)

  assert t3 == [2,4,4,5,99,9801], f"t3 {t3}"

  t4 = [1,1,1,4,99,5,6,0,99]
  compute(t4, 0)

  assert t4 == [30,1,1,4,2,5,6,0,99], f"t4 {t4}"

  t5 = [1,9,10,3,2,3,11,0,99,30,40,50]
  compute(t5, 0)

  assert t5 == [3500,9,10,70,2,3,11,0,99,30,40,50], f"t5 {t5}"

  print("ok")