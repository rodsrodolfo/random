from PIL import Image

print('Example:\nFile: Photo1.png (with format)\nTake: 255 144 207 255\nPut: 0 86 133 255\nNew name: NewFilename (without format)\n')
filename = input('File:')

image=Image.open(filename)
pixels1=image.convert('RGBA').load()
pixels2=[]
width, height = image.size

pixel1=tuple(map(int,input('Take: ').split()))
pixel2=tuple(map(int,input('Put: ').split()))
newname=input('New name: ')

for a in range(height):
    for b in range(width):
        if pixels1[b,a]==pixel1:
            pixels2.append(pixel2)
        else:
            pixels2.append(pixels1[b,a])

image.putdata(pixels2)
image.save(newname+'.png')
