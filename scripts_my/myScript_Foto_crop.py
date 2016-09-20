# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFilter

def foto_crop(_foto):
    try:
        image = Image.open(_foto)                       
    except IOError:
        print "don't treat"
        #continue
    #image = image.resize((541, 538))
    width = image.size[0] 			#Определяем ширину.
    height = image.size[1] 			#Определяем высоту.
    
    sum = Image.new( 'RGB', (width, width) , (255,255,255)) # create a new white image 
    if height >= width:
        #sum = Image.new( 'RGB', (width, width) , (255,255,255)) # create a new white image 
        print u"height is higher"
        diff = height - width     
        for i in xrange(width):
            for j in xrange(width):
                pixel = image.getpixel((i,j+(diff/2)))
                sum.putpixel((i,j),pixel)
        #sum.save(_foto)   # перезаписываем первоначальный файл 
    else:  # height < width:
        #sum = Image.new( 'RGB', (height, height) , (255,255,255)) # create a new white image 
        print u"width is higher"
        diff = width - height
        for i in xrange(height):
            for j in xrange(height):
                pixel = image.getpixel((i+(diff/2),j))
                sum.putpixel((i,j),pixel)
    sum.filter(ImageFilter.MedianFilter(size=3))
    sum.save(_foto)


foto_crop('test.jpg')


print "###############################################################################################"








                
