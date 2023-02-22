from PIL import Image
import sys

if len(sys.argv) >= 2 :
    name = sys.argv[1]
else:
    name = input("Enter A Name: ")

ascii_name = [ord(c) for c in name]
l = len(ascii_name)

x = 0
for i in ascii_name:
    x += i

x = x *10000 + x * 10000 + x
print(x)
colour = [int(str(x)[:3]) % 256, int(str(x)[int(len(str(x))/2):int((len(str(x))/2)+3)]) % 256, int(str(x)[6:]) % 256]
print(colour)


img = Image.new('RGB', [l,l], (255, 255, 255))
data = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if ascii_name[(x+y)%l] % 3 == 0:
            data[x,y] = (colour[0], colour[1], colour[2])
        # data[x,y] = (ascii_name[x%l], ascii_name[y%l], ascii_name[(x+y)%l])

img.save('image.png')
