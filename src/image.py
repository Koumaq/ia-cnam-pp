from PIL import Image, ImageFilter

image = Image.open("/Users/pokem/PycharmProjects/ia-cnam-pp/image/Designer.jpeg")

resized_img = image.resize((300, 200))
rotate_img = image.rotate(90)
blurred_img = image.filter(ImageFilter.BLUR)

print("fin")
