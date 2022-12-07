from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    
    button1 = browser.find_element(By.ID, "book")
    sotka = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1.click()
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
   
       
    button2 = browser.find_element(By.ID, 'solve')
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

