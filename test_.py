class chia_nhi:
	str1 =''
	str2 =''
	length_bit = 0
	K = None
	Q = None
	H = None
	thuong = ''
	def __init__(self,a,b):
		for i in a:
			if(i == '0' or i == '1' ):
				self.str1 += i
		for i in b:
			if(i == '0' or i == '1' ):
				self.str2 += i
		
		
		if(len(self.str1) > 16  or len(self.str2) > 16  ):
			self.length_bit= 32
		else:
			self.length_bit= 16
	def ket_qua(self):
		#1
		self.str1 = self.cchuan_hoa(self.str1,self.length_bit)
		#2
		self.K = self.ck()
		self.Q = self.str1
		self.Q= self.cchuan_hoa(self.Q,self.length_bit)
		#3
		self.H = self.ccong(self.K , self.Q)
		
		self.H = self.cchuan_hoa(self.H,self.length_bit)
		
		if(int(self.H[0])):
			self.thuong += '0'
		else:
			self.thuong += '1'
			self.Q = self.H
		#4
		self.dich_k()
		print("K = ",self.K)
		print("H = K + Q = ",self.H,"\t\t","thương :",self.thuong[len(self.thuong)-1],end="\n\n")
		while(self.nhi_str_to_thap_int(self.H) != 0 and self.nhi_str_to_thap_int(self.H) > self.nhi_str_to_thap_int(self.str2)):
			#3
			self.H = self.ccong(self.K , self.Q)
			print(self.H)
			if(int(self.H[0])):
				self.thuong += '0'
			else:
				self.thuong += '1'
				self.Q = self.H
			#4
			self.dich_k()
			print("K = ",self.K)
			print("H = K + Q = ",self.H,"\t\t","thương :",self.thuong[len(self.thuong)-1],end="\n\n")
		#5
		print("-------------------------------------------------------------------")
		print("Vậy ta có kết quả = ",self.thuong," = ",self.nhi_str_to_thap_int(self.thuong),"\n","Số dư H = ",self.H," = ",self.nhi_str_to_thap_int(self.H))
	def dich_k(self):
		self.K = self.K[0] + self.K[0:len(self.K) -1]

	def cchuan_hoa(self,s,l):
		return '0'*(l-len(s)) + s
		
	def ck(self):
		nhi = self.str2
		bu1 = ''
		for i in nhi:
			bu1 += str(1- int(i))
		bu2 = self.thap_int_to_nhi_str( self.nhi_str_to_thap_int(bu1) + 1 )
		if (len(bu2) < 8 ):
			bu2 = self.cchuan_hoa(bu2,8)
			result = bu2[4:8]
		elif (len(bu2) < 16 ):
			bu2 = self.cchuan_hoa(bu2,16)
			result = bu2[8:16]
		
		return result + ( '0'*int(self.length_bit/2) )

	
	def nhi_str_to_thap_int(self,s):
		dem = 0
		result = 0
		run = len(s)-1
		while(run >= 0 ):
			if(s[run]== '1'):
				result += 2**dem
				dem+=1
			elif(s[run]=='0'):
				dem+=1
			else:
				pass
			run-=1
		return result

	def thap_int_to_nhi_str(self,s):
		result=[]
		while(s > 0):
			if(s - int(s/2)*2):
				result.append('1')
			else:
				result.append('0')
			s = int( s / 2 )
		run = len(result)-1
		nhi = ''
		while(run >= 0):
			nhi += result[run]
			run -= 1
		return nhi
	def ccong(self,a,b):
		re = self.thap_int_to_nhi_str(self.nhi_str_to_thap_int(a) + self.nhi_str_to_thap_int(b))
		if(len(re) > 16):
			re= re[len(re)-16:len(re)]
		return re
if __name__ == '__main__':
	chia_nhi('0000 0000 0101 1111b','0000 0111b').ket_qua()