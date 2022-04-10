from PIL import Image
import time
img =  Image.open("C:\\Users\\tiepl\\Desktop\\images.jpg")
img = img.convert('1')
row,col = img.size
img_data = img.getdata()
dem=0

for i in img_data:
	if(i==0):
		print("  ",end="")
	if(i==255):
		print("♥♥",end="")
	dem+=1
	if(dem %row ==0):
		print("")
time.sleep(9999)
