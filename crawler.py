from bs4 import BeautifulSoup as bts
from selenium import webdriver

driver = webdriver.Firefox()
url = "https://www.lazada.vn/dien-thoai-di-dong/?page=1"
driver.get(url)
root = driver.find_element_by_id(id_='root')
# print(root.get_attribute('innerHTML'))
lzd = root.get_attribute('innerHTML')
soup = bts(lzd, 'lxml')
# print(soup.title.string)
products = soup.find_all(class_='c2prKC')
# print(products)
# print(lzd.text)
count = 0
for product in products:
	# if product.has_attr('class'):
	count += 1
print(count)
driver.close()