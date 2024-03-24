from PIL import Image

img = Image.open('i-125-13.jpeg')

new_img = img.resize((800, 600))
new_img.save('i-125-13.jpeg')