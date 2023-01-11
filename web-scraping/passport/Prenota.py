from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Prenota:

    def __init__(self):
        opt = Options()
        opt.add_experimental_option("detach",True) #doesnt close chrome after finishing
        self.driver = webdriver.Chrome(options=opt)

    def login(self, user, pword):
        self.driver.get("https://prenotami.esteri.it/Services")
        login = self.driver.find_element(By.ID,"login-email")
        login.send_keys(user)
        password = self.driver.find_element(By.ID,"login-password")
        password.send_keys(pword)
        self.driver.find_element(By.XPATH,"//*[@id='login-form']/button").click()

    def pressPrenota(self):
        prenota_xpath = "//*[@id='dataTableServices']/tbody/tr[1]/td[4]/a/button"
        self.driver.find_element(By.XPATH, prenota_xpath).click()
