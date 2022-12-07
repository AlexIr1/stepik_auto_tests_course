from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
 
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    z_element = browser.find_element(By.ID, "num2")
    z = z_element.text
    y = str(int(x)+int(z))
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)
   
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

