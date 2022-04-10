from PIL import Image
import os

'''
if os.path.exists("C:\\Users\\tiepl\\Desktop\\anh_captcha_google\\w"+str(s)+".png"):
	s += 1
	continue
'''
if __name__ == '__main__':
	s = 0
	anh300 = 5922
	anh450 = 2596
	while(s < 39322):
		if os.path.exists("C:\\Users\\tiepl\\Desktop\\anh_captcha_google\\w"+str(s)+".png"):
			img =  Image.open("C:\\Users\\tiepl\\Desktop\\anh_captcha_google\\w"+str(s)+".png")
			s += 1
			row,col = img.size
			if(row == 300):
				#img.save("C:\\Users\\tiepl\\Desktop\\300x300_9\\w"+str(anh300)+".png",'PNG')
				#anh300 += 1
				pass
			elif(row == 450):
				#img.save("C:\\Users\\tiepl\\Desktop\\450x450_16\\w"+str(anh450)+".png",'PNG')
				#anh450 += 1
				pass
			else:
				print("===============================================================>",s)
			img.close()
			continue
		s += 1
	print("xong")
	input()
		
		

