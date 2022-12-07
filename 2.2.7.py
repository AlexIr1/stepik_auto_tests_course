from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
 
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    option1 = browser.find_element(By.CSS_SELECTOR, ".form-check-label")
    option1.click()
    
    #browser.execute_script("window.scrollBy(0, 100);")
    
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

