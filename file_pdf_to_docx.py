# -*- coding: utf-8 -*-
import fitz,re,os
import pytesseract as pt
from pytesseract import image_to_string
import docx
from PIL import Image
pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\Tesseract.exe'

doc = fitz.open(r'C:\Users\tiepl\Desktop\Giao-trinh-Chu-Nghia-Xa-Hoi-Khoa-Hoc-CNXHKH-TailieuVNU.com_.pdf')

# for pg in range(doc.pageCount):
# 	page = doc[pg]
# 	rotate = int(0)  
# 	zoom_x = 2.0
# 	zoom_y = 2.0
# 	trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
# 	pm = page.getPixmap(matrix=trans, alpha=False)
# 	pm.writePNG('D:\\%s.png' % pg)
# print("successful")

mydoc = docx.Document()
i=0
while(i < doc.pageCount):
	new_img =  Image.open("D:\\"+str(i)+".png")
	print(str(i)+".png")
	text = image_to_string(new_img, lang="vie")
	kt=text[len(text)-1]
	text = re.sub( kt, '', text)
	mydoc.add_paragraph(text)
	os.remove("D:\\"+str(i)+".png")
	i+=1

mydoc.save(r"C:\Users\tiepl\Desktop\Giao-trinh-Chu-Nghia-Xa-Hoi-Khoa-Hoc-CNXHKH-TailieuVNU.com_.docx")
