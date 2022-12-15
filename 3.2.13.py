from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestReg(unittest.TestCase):
     
     def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
   
   
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        input1.send_keys("1")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        input2.send_keys("2")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        input3.send_keys("3")
        time.sleep(2)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'ne uspeshno')

     
     
     def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
   
   
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        input1.send_keys("1")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        input2.send_keys("2")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        input3.send_keys("3")
        time.sleep(5)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)

if __name__ == "__main__":
    unittest.main()