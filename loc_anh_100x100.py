
from PIL import Image
import os

if __name__ == '__main__':
	run =0
	anh100 = 0
	lstbig = []
	dem=0
	while(run < 11):
		if(run % 500 == 0):
			print(run)
		if os.path.exists("C:\\Users\\tiepl\\Desktop\\100x100\\"+str(run)+".png"):
			img =  Image.open("C:\\Users\\tiepl\\Desktop\\100x100\\"+str(run)+".png")#đã có ảnh 
			run += 1
			img = img.convert("1")
			img = img.crop()
			#bat dau ghi
			lst = []
			img_data = img.getdata()
			for i in img_data:
				lst.append(i)
			for ide in range(0,len(lstbig) - 1):
				if(ide == lst):
					print("lap",dem)
					dem += 1
					img.close()
					continue
			lstbig.append(lst)
			img.close()
			continue
		run += 1
	# ta đã có lstbig -> sap xep thoi
	print("da nap xong image")
	lstbig.sort()
	print("da xap xep xong")
	print(len(lstbig))
	input()
	for listanh in lstbig:
		new_img = Image.new(mode = "RGB",size= [100,100])
		new_img.putdata(listanh)
		new_img.save('D:\\New folder\\w'+str(anh100)+'.png','PNG')#  save
		anh100 += 1
