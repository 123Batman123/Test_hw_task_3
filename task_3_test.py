import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


login_ya = ''
password_ya = ''


class TestSeleniumAuth(unittest.TestCase):
    def setUp(self):
        s = Service('C:/Py/practical_work/test_hw_task_3/chromedriver/chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def test_auth_yandex(self):
        url = 'https://passport.yandex.ru/auth/'
        driver = self.driver
        driver.get(url=url)
        time.sleep(5)
        id_email = driver.find_element(By.ID, "passp-field-login")
        id_email.clear()
        id_email.send_keys(login_ya + Keys.ENTER)
        time.sleep(5)
        id_password = driver.find_element(By.ID, "passp-field-passwd")
        id_password.clear()
        id_password.send_keys(password_ya + Keys.ENTER)
        time.sleep(10)
        self.assertEqual(driver.title, 'Яндекс ID')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
