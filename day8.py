def get_rows(layer, width, height):
  rows = []
  pointer = 0
  for i in range(height):
    end_pointer = pointer + width
    rows.append(layer[pointer:end_pointer])
    pointer = end_pointer
  return rows


def get_layers(image, width, height):
  size = len(image)
  layer_size = width * height
  layers = []
  pointer = 0
  while pointer < len(image):
    end_pointer = pointer + layer_size
    layer = get_rows(image[pointer:end_pointer], width, height)
    layers.append(layer)
    pointer = end_pointer
  return layers

def count_zeros(layer):
  return count_numbers(layer, '0')

def count_numbers(layer, number):
  x = sum(map(lambda row : row.count(number), layer)) 
  return x

def main():
  file = open("input8.txt")
  input = file.read()
  file.close()

  layers = get_layers(input, 25, 6)
  check_layer = min(layers, key=count_zeros)
  result = count_numbers(check_layer, '2') * count_numbers(check_layer, '1') 
  print(result)

def test():
  t_in = "123456789012"
  t = get_layers(t_in, 3, 2)
  expected = [ [ "123", "456" ], [ "789", "012" ] ]

  assert t == expected, f"{t}"

  print("ok")