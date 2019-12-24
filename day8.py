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

def get_image(layers, width, height):
  image = [[0 for i in range(width)] for j in range(height)]

  for i in range(height):
    for j in range(width):
      for l in layers:
        if l[i][j] != '2':
          if l[i][j] == "0":
            image[i][j] = " "
          else:
            image[i][j] = "0"
          break  
  return image

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
  image = get_image(layers, 25, 6)
  for row in image:
    r = ''.join(row)
    print(r)

def test():
  t_in = "0222112222120000"
  l = get_layers(t_in, 2, 2)
  t = get_image(l, 2, 2)
  print(t)