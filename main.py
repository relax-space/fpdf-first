'''
解决目标: 0001.jpg 本来是png格式,但是被篡改成了jpg
'''

import os

from fpdf import FPDF
from PIL import Image


def get_ext(img_path: str):
    return Image.open(img_path).format


def main():
    try:

        pdf = FPDF(orientation='L', unit='pt', format='legal')
        pdf.set_auto_page_break(0)

        width, height = 800, 1100
        folder_name = 'i1'
        for i in os.listdir(folder_name):
            file_path = os.path.join(folder_name, i)
            ext = get_ext(file_path)
            pdf.add_page()
            pdf.image(file_path, type=ext, w=width, h=height)
        pdf.output('1.pdf', "F")
        return 0
    except Exception as e:
        print(e)
        return -1


if __name__ == '__main__':
    print(main())
