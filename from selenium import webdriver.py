from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import pytesseract as pt

pt.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\Tesseract.exe'


def initDriver(filepath):

	options = webdriver.ChromeOptions()
	options.add_argument(r'user-data-dir=c:\withpython\\'+ filepath) 
	'''
	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	options.add_experimental_option("prefs", prefs)
	'''
	browser = webdriver.Chrome(executable_path=r'c:\withpython\chromedriver.exe', chrome_options=options)
	return browser 

tang=0
if __name__ == '__main__':
	while(1):
		taikhoan =  ("tieple247",'tieple01','tieple02','tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13','tieple15','tieple16','tieple17')
		taikhoanx = taikhoan[tang]
		driver = initDriver(taikhoanx)
		driver.get("https://www.typingstudy.com/vi-vietnamese_vni-3/typingtest")
		#text_input=" Khái niệm hàng hóa: Hàng hóa là sản phẩm của lao động, có thể thỏa mãn nhu cầu nào đó của con người thông qua trao đổi, mua bán.2.2.1.2. Thuộc tính của hàng hóa- Giá trị sử dụng của hàng hóaGiá trị sử dụng của hàng hóa là công dụng của sản phẩm, có thể thỏa mãn nhu cầu nào đó của con người.Nhu cầu đó có thể là nhu cầu vật chất hoặc nhu cầu tinh thần; có thể là nhu cầu cho tiêu dùng cá nhân, có thể là nhu cầu cho sản xuất.Đặc điểm giá trị sử dụng chỉ được thực hiện trong việc sử dụng hay tiêu dùng. Nền sản xuất càng phát triển, khoa học, công nghệ càng hiện đại, càng giúp cho con người phát hiện ra nhiều và phong phú hơn các giá trị sử dụng của sản phẩm.Giá trị sử dụng của hàng hóa là giá trị sử dụng nhằm đáp ứng yêu cầu của người mua. Cho nên, nếu là người sản xuất, phải chú ý hoàn thiện giá trị sử dụng của hàng hóa do mình sản xuất ra sao cho ngày càng đáp ứng nhu cầu khắt khe và tinh tế hơn của người mua.- Giá trị của hàng hóaĐể nhận biết được thuộc tính giá trị, xét trong quan hệ trao đổi.Thí dụ, có một quan hệ trao đổi như sau: 1 mét vải = 10 kg gạoTỷ lệ trao đổi giữa các giá trị sử dụng khác nhau này được gọi là giá trị trao đổi.Vấn đề đặt ra là: tại sao giữa các hàng hóa có giá trị sử dụng khác nhau lại trao đổi được với nhau, với những tỷ lệ nhất định Sở dĩ các hàng hóa trao đổi được với nhau là vì giữa chúng có một điểm chung. Điểm chung đó không phải là giá trị sử dụng mặc dù giá trị sử dụng là yếu tố cần thiết để quan hệ trao đổi được diễn ra. Điểm chung đó phải nằm ở trong cả hai hàng hóa.Nếu gạt giá trị sử dụng hay tính có ích của các sản phẩm sang một bên thì giữa chúng có điểm chung duy nhất chúng đều là sản phẩm của lao động; một lượng lao động bằng nhau đã hao phí để tạo ra số lượng các giá trị sử dụng trong quan hệ trao đổi đó.Giá trị là lao động xã hội của người sản xuất hàng hóa kết tinh trong hàng hóa.Giá trị hàng hóa biểu hiện mối quan hệ kinh tế giữa những người sản xuất, trao đổi hàng hóa và là phạm trù có tính lịch sử.Giá trị trao đổi là hình thức biểu hiện ra bên ngoài của giá trị, giá trị là nội dung, là cơ sở của trao đổi. Khi trao đổi người ta ngầm so sánh lao động đã hao phí ẩn dấu trong hàng hóa với nhau. Mối quan hệ giữa hai thuộc tính của hàng hóaMối quan hệ giữa giá trị và giá trị sử dụng là mối quan hệ thống nhất của của hai mặt đối lập. Do vậy có quan hệ thống nhất và quan hệ mâu thuẫn.- Thống nhất: đã là hàng hóa phải có đủ hai thuộc tính- Mâu thuẫn:+ Người làm ra đem bán chỉ quan tâm đến giá trị hàng hóa do mình làm ra. Ngược lại, người mua lại chỉ chú ý đến giá trị sử dụng của hàng hóa+ Giá trị được tạo ra trong sản xuất và được thực hiện trong lưu thông; giá trị sử dụng được thực hiện trong quá trình tiêu dùng+ Giá trị đồng nhất về chất; giá trị sử dụng không đồng nhất về chấtTrong thực hiện sản xuất hàng hóa, để thu được hao phí lao động đã kết tinh (giá trị) người sản xuất phải chú ý hoàn thiện giá trị sử dụng để được thị trường chấp nhận. Hàng hóa phải được bán đi, ngược lại người sản xuất sẽ bị thua lỗ thậm chí phá sản.2.2.3. Lượng giá trị và các nhân tố ảnh hưởng đến lượng giá trị của hàng hóa2.2.3.1. Lượng giá trị của hàng hóa Giá trị của hàng hóa là do lao động xã hội, trừu tượng của người sản xuất ra hàng hóa kết tinh trong hàng hóa. Vậy lượng giá trị của hàng hóa là lượng lao động đã hao phí để tạo ra hàng hóa. Lượng lao động đã hao phí được tính bằng thời gian lao động. Thời gian lao động này phải được xã hội chấp nhận, không phải là thời gian lao động của đơn vị sản xuất cá biệt, mà là thời gian lao động xã hội cần thiết.Thời gian lao động cá biệt là thời gian hao phí để sản xuất ra một hàng hóa của từng người, từng doanh nghiệp. Do điều kiện sản xuất khác nhau, trình độ tay nghề khác nhau vì thế thời gian lao động cá biệt để sản xuất ra hàng hóa của từng người, từng doanh nghiệp cũng khác nhau.Thời gian lao động xã hội cần thiết là thời gian đòi hỏi để sản xuất ra một giá trị sử dụng nào đó trong những điều kiện bình thường của xã hội với trình độ thành thạo trung bình, cường độ lao động trung bình.2.2.3.2.Các nhân tố ảnh hưởng đến lượng giá trị của hàng hóaTất cả những nhân tố ảnh hưởng tới lượng thời gian hao phí xã hội cần thiết để sản xuất ra một đơn vị hàng hóa thì sẽ ảnh hưởng tới lượng giá trị của đơn vị hàng hóa. Có những nhân tố chủ yếu sau:Một là, năng suất lao động,Năng suất lao động là là năng lực sản xuất của người lao động, được tính bằng số lượng sản phẩm sản xuất ra trong một đơn vị thời gian, hay số lượng thời gian hao phí để sản xuất ra một đơn vị sản phẩm.Năng suất lao động tăng lên sẽ làm giảm lượng thời gian hao phí lao động cần thiết trong một đơn vị hàng hóa, làm cho lượng giá trị trong một đơn vị hàng hóa giảm xuống.Các nhân tố ảnh hưởng đến năng suất lao động gồm: 1) trình độ khéo léo trung bình của người lao động; 2) mức độ phát triển của khoa học và trình độ áp dụng khoa học vào quy trình công nghệ; 3) sự kết hợp xã hội của quá trình sản xuất ; 4) quy mô và hiệu suất của tư liệu sản xuất; 5) các điều kiện tự nhiên,Khi xem xét về mối quan hệ giữa tăng năng suất với lượng giá trị của một đơn vị hàng hóa, cần chú ý thêm về mối quan hệ giữa tăng cường độ lao động với lượng giá trị của một đơn vị hàng hóa.Cường độ lao động là mức độ khẩn trương, tích cực của hoạt động lao động trong sản xuất.Tăng cường độ lao động là tăng mức độ khẩn trương, tích cực của hoạt động lao động. Tăng cường độ lao động làm cho tổng số sản phẩm tăng lên. Tổng lượng giá trị của tất cả các hàng hóa gộp lại tăng lên. Song, lượng thời gian lao động xã hội cần thiết hao phí để sản xuất một đơn vị hàng hóa không thay đổi.Cường độ lao động chịu ảnh hưởng của các yếu tố sức khỏe, thể chất, tâm lý, trình độ tay nghề thành thạo của người lao động, công tác tổ chức, kỷ luật lao động... Nếu giải quyết tốt những vấn đề này thì người lao động sẽ thao tác nhanh hơn, thuần thục hơn, tập trung hơn, do đó tạo ra nhiều hàng hóa hơn.hai là, tính chất phức tạp của lao động.Căn cứ vào mức độ phức tạp của lao động mà chia thành lao động giản đơn và lao động phức tạp.Lao động giản đơn là lao động không đòi hỏi có quá trình đào tạo một cách hệ thống, chuyên sâu về chuyên môn, kỹ năng, nghiệp vụ cũng có thể thao tác được.Lao động phức tạp là những hoạt động lao động yêu cầu phải trải qua một quá trình đào tạo về kỹ năng, nghiệp vụ theo yêu cầu của những nghề nghiệp chuyên môn nhất định.Trong cùng một đơn vị thời gian lao động như nhau, lao động phức tạp tạo ra nhiều giá trị hơn so với lao động giản đơn."
		text_input = str (input ())
		dem=0
		for i in text_input:
			driver.find_element_by_name("type").send_keys(i)
			print(i)
			time.sleep(0.1)
			dem+=1
			if(dem == 6 ):
				dem =0
				time.sleep(random.randint(0,1))
		input()
		#time.sleep(2)
		try:
			driver.quit()
		except:
			time.sleep(0)
		tang+=1