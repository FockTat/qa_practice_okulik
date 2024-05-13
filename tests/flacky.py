from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://magento.softwaretestingboard.com/women/tops-women/tees-women.html')
# явное ожидание
wait = WebDriverWait(browser, 10)
wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), "Support This Project"))


girls = browser.find_elements(By.CLASS_NAME, 'product-item-link')
first_girl = girls[0]  # ищет первый элемент в списке

print(first_girl.text)
print(first_girl.get_attribute('href'))

# для выбора элемента из выпадающего списка
sorter = browser.find_element(By.ID, 'sorter')  # элемент из выподающего списка
select = Select(sorter)
select.select_by_value('price')
wait.until(EC.staleness_of(first_girl))  # при смене элементов на новой странице
girls = browser.find_elements(By.CLASS_NAME, 'product-item-link')
first_girl = girls[0]
print(first_girl.text)
print(first_girl.get_attribute('href'))
