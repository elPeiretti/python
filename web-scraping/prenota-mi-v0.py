from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

USER = ""
PWORD = ""

def login(driver):
    driver.get("https://prenotami.esteri.it/Services")


    login = driver.find_element(By.ID,"login-email")
    login.send_keys(USER)
    password = driver.find_element(By.ID,"login-password")
    password.send_keys(PWORD)
    driver.find_element(By.XPATH,"//*[@id='login-form']/button").click()
    


def pressPrenota(driver):
    prenota_xpath = "//*[@id='dataTableServices']/tbody/tr[1]/td[4]/a/button"

    # waits 20 seconds until prenota button loads and is clickable
    try:
        elem = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, prenota_xpath))
        )
    finally:
        driver.find_element(By.XPATH, prenota_xpath).click()

def success(driver):
    not_available_ok = "/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button"
    message_class = "jconfirm-content"
    not_available_message = "Al momento non ci sono date disponibili per il servizio richiesto"
    
    try:
        elem = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, message_class))
            )
    finally:
        message = driver.find_element(By.CLASS_NAME, message_class).find_element(By.TAG_NAME,"div").get_attribute("innerHTML").strip()
    
    if message == not_available_message:
        driver.find_element(By.XPATH,not_available_ok).click()
    
    return message != not_available_message
    
    

if __name__ == "__main__":

    driver = webdriver.Chrome()
    logging.basicConfig(filename="prenota-log.txt",level=logging.DEBUG)

    login(driver)
    pressPrenota(driver)

    while not success(driver):
        driver.get("https://prenotami.esteri.it/Services")
        try:
            pressPrenota(driver)
        except Exception as e:
            logging.debug(e)


    driver.quit()