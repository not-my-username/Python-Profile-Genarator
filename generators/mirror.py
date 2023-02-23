from PIL import Image, ImageOps
import sys
import random

if len(sys.argv) >= 2 :
    name = sys.argv[1]
else:
    name = input("Enter A Name: ")

size = 11

ascii_name = [ord(c) for c in name]
l = len(ascii_name)

x = 0
for i in ascii_name:
    x += i

x = x *10000 + x * 10000 + x
colour = [int(str(x)[:3]) % 256, int(str(x)[int(len(str(x))/2):int((len(str(x))/2)+3)]) % 256, int(str(x)[6:]) % 256]

random.seed(x)

img = Image.new('RGB', [size, size], (255, 255, 255))
data = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if ascii_name[(x+y)%l] % 3 == 0:
            data[x,y] = (colour[0], colour[1], colour[2])

for x in range(img.size[0]):
    for y in range(img.size[1]):
        for z in range(1, size):
            print(z, size)
            data[size - z, y -1] = data[z - 1, y-1]

print()

img.save('./image.png')