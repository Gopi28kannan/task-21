from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class webpage:
     #some security purpose. So your enter own email id and password
     Email = "enter your email"
     Password = "enter your password"
     def __init__(self, url):
          self.url = url
          self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     def logins(self):
          try:
               self.driver.get(self.url)
               #self.driver.maximize_window()
               print("cookies collected in before login : \n",self.driver.get_cookies(),'\n\n')
               time.sleep(2)
               self.driver.find_element(By.NAME,"email").send_keys(self.Email)
               time.sleep(2)
               self.driver.find_element(By.NAME,"password").send_keys(self.Password)
               time.sleep(2)
               login_process=self.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
               time.sleep(2)
               print("cookies collected in after login : \n",self.driver.get_cookies(),'\n\n')
               time.sleep(3)
               self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/nav/ul/div[2]/li/span/div').click()
               print("cookies collected in dashboard: \n",self.driver.get_cookies(),'\n\n')
               time.sleep(4)
               self.driver.find_element(By.CSS_SELECTOR,'img[class="profileIcon"]').click()
               time.sleep(2)
               self.driver.find_element(By.XPATH,'//*[@id="root"]/nav/div/div/div/div/button[2]').click()
               print("cookies collected in after logout : \n",self.driver.get_cookies())
          except:
               print('error')
          finally:
               print("\n\nsucessfully executed")
     def shutdown(self):
          time.sleep(10)
          self.driver.quit()
url = "https://www.zenclass.in/login"
wb=webpage(url)
wb.logins()
wb.shutdown()    
