from PIL import Image

name = 'cnrs'
format = 'png'

pixel1=(255,255,255,255)
pixel2=(255,255,255,0)

with Image.open(f'{name}.{format}') as image:
	width, height = image.size

	pixels1=image.convert('RGBA').load()
	pixels2=[]

	for a in range(height):
	    for b in range(width):
	        if pixels1[b,a][2]<50:
	            pixels2.append(pixel2)
	        else:
	            pixels2.append(pixels1[b,a])

print(pixels1[5,5])

with Image.new('RGBA', (width, height)) as image2:
	image2.putdata(pixels2)
	image2.save(f'{name}_new.png')
