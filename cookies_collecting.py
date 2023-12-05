from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class webpage:
     username = "problem_user"
     password = "secret_sauce"
     def __init__(self, url):
          self.url = url
          self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     def login_logout(self):
          try:
               self.driver.get(self.url)
               self.driver.maximize_window()
               #cookies collect before login
               print("cookies collect in before login : \n",self.driver.get_cookies())
               #create in new line
               print()
               time.sleep(2)
               self.driver.find_element(By.NAME,"user-name").send_keys(self.username)
               time.sleep(2)
               self.driver.find_element(By.NAME,"password").send_keys(self.password)
               time.sleep(2)
               #cookies collect after login
               login_process=self.driver.find_element(By.CSS_SELECTOR,'input[id="login-button"]').click()
               print("cookies collect in after login : \n",self.driver.get_cookies())
               print()
               time.sleep(2)
               #cookies collect after logout
               self.driver.find_element(By.XPATH,'//*[@id="react-burger-menu-btn"]').click()
               time.sleep(2)
               self.driver.find_element(By.LINK_TEXT,'Logout').click()
               print("cookies collect in after logout : \n",self.driver.get_cookies())
          except:
               print('error')
     def shutdown(self):
          time.sleep(4)
          self.driver.quit()
url="https://www.saucedemo.com/"
wb=webpage(url)
wb.login_logout()
wb.shutdown()
