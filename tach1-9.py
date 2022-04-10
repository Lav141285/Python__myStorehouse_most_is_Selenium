
from PIL import Image
import os

if __name__ == '__main__':
	run =0
	anh100 = 0
	while(run<27589):
		if(run % 500 == 0):
			print(run)
		if os.path.exists("C:\\Users\\tiepl\\Desktop\\300x300_9\\w"+str(run)+".png"):
			img =  Image.open("C:\\Users\\tiepl\\Desktop\\300x300_9\\w"+str(run)+".png")#đã có ảnh 
			run += 1
			row,col = img.size #đã có kích thước

			im1 = img.crop((0,0, 100,100))
			im2 = img.crop((100,0,200,100))
			im3 = img.crop((200,0, 300,100))

			im4 = img.crop((0,100, 100,200))
			im5 = img.crop((100,100, 200,200))
			im6 = img.crop((200,100, 300,200))

			im7 = img.crop((0,200, 100,300))
			im8 = img.crop((100,200, 200,300))
			im9 = img.crop((200,200, 300,300))
			
			im1.save('C:\\Users\\tiepl\\Desktop\\100x100_1\\w'+str(anh100)+'.png','PNG')
			anh100+=1
			im2.save('C:\\Users\\tiepl\\Desktop\\100x100_1\\w'+str(anh100)+'.png','PNG')
			anh100+=1
			im3.save('C:\\Users\\tiepl\\Desktop\\100x100_1\\w'+str(anh100)+'.png','PNG')
			anh100+=1
			im4.save('C:\\Users\\tiepl\\Desktop\\100x100_1\\w'+str(anh100)+'.png','PNG')
			anh100+=1
			im5.save('C:\\Users\\tiepl\\Desktop\\100x100_1\\w'+str(anh100)+'.png','PNG')
			anh100+=1
			im6.save('C:\\Users\\tiepl\\Desktop\\100x100_1\\w'+str(anh100)+'.png','PNG')
			anh100+=1
			im7.save('C:\\Users\\tiepl\\Desktop\\100x100_1\\w'+str(anh100)+'.png','PNG')
			anh100+=1
			im8.save('C:\\Users\\tiepl\\Desktop\\100x100_1\\w'+str(anh100)+'.png','PNG')
			anh100+=1
			im9.save('C:\\Users\\tiepl\\Desktop\\100x100_1\\w'+str(anh100)+'.png','PNG')
			anh100+=1
			

			img.close()
			continue
		run += 1
	print("xong")
	input()