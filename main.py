from PIL import Image

name = "Liam Sherwin"
ascii_name = [ord(c) for c in name]
l = len(ascii_name)
colour = ascii_name[0] + ascii_name[1] + ascii_name[2]


img = Image.new('RGB', [l,l], (255, 255, 255))
data = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if ascii_name[(x+y)%l] % 3 == 0:
            data[x,y] = (ascii_name[0], ascii_name[1], ascii_name[2])
        # data[x,y] = (ascii_name[x%l], ascii_name[y%l], ascii_name[(x+y)%l])

img.save('image.png')
