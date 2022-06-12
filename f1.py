import os

import img2pdf
from PIL import Image

# storing image path
img_path = "imgs/0001.jpg"

# storing pdf path
pdf_path = "1.pdf"

# opening image
image = Image.open(img_path)

folder_name = 'i1'
file_path_list = [os.path.join(folder_name, i)
                  for i in os.listdir(folder_name)]
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(file_path_list)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")
