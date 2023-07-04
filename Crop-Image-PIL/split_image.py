from PIL import Image

img = Image.open("D:\\CU\\MRI_3D_to_2D\\test.jpg")
img.show(5)


width, height = img.size


# 1st part
left = 0
top = 0
right = width/2
bottom = height/2

img1 = img.crop((left,top,right,bottom))

img1 = img1.save("D:\\CU\\MRI_3D_to_2D\\test1.jpg")
image_open = Image.open("D:\\CU\\MRI_3D_to_2D\\test1.jpg")
image_open.show()


# 2nd part
left = width/2
top = 0
right = width
bottom = height/2

img2 = img.crop((left,top,right,bottom))

img2 = img2.save("D:\\CU\\MRI_3D_to_2D\\test2.jpg")
image_open = Image.open("D:\\CU\\MRI_3D_to_2D\\test2.jpg")
image_open.show()


# 3rd part
left = 0
top = height/2
right = width/2
bottom = height

img3 = img.crop((left,top,right,bottom))

img3 = img3.save("D:\\CU\\MRI_3D_to_2D\\test3.jpg")
image_open = Image.open("D:\\CU\\MRI_3D_to_2D\\test3.jpg")
image_open.show()


# 4th part
left = width/2
top = height/2
right = width
bottom = height

img4 = img.crop((left,top,right,bottom))

img4 = img4.save("D:\\CU\\MRI_3D_to_2D\\test4.jpg")
image_open = Image.open("D:\\CU\\MRI_3D_to_2D\\test4.jpg")
image_open.show()










