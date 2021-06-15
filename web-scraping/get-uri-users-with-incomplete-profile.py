import pandas
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium import common
import time
from datetime import date
from datetime import datetime

# https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
# pip install openpyxl


def getDriver():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    time.sleep(2)
    return driver

def validateProfile(id,driver):
    
    driver.get("https://www.urionlinejudge.com.br/judge/en/profile/"+id)
    print(id)

    try:
        pais = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/ul/li[2]")
        uni = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/ul/li[3]")
    
    except common.exceptions.NoSuchElementException: # no existe el usuario
        return -1 

    if "AR" in pais.get_attribute('innerHTML') and "UTN" in uni.get_attribute('innerHTML'):
        return 1

    return 0


######## main ###########

DRIVER = getDriver()

# reads .csv file obtained from urionlinejudge.com.br/academic/
col_list = ["uri","student","email"]
data = pandas.read_csv("planilla.csv", sep=';', usecols=col_list)
listado = {
    'Estudiante': [],
    'Email': []
}

for i in range (len(data)):
    id =data.loc[i,"uri"]
    if validateProfile(str(id),DRIVER)==0:
        listado.get('Estudiante').append(data.loc[i,"student"])
        listado.get('Email').append(data.loc[i,"email"])

pandas.DataFrame(listado, columns=["Estudiante","Email"]).to_excel("excel.xlsx", index = False, header=True)
DRIVER.quit()

#elPeiretti
