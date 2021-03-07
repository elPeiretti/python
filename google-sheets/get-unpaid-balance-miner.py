from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from datetime import datetime

##
## GECKODRIVER PATH ERROR SOLUTION https://askubuntu.com/questions/851401/where-to-find-geckodriver-needed-by-selenium-python-package
## pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
## pip install oaut2client time datetime gspread selenium
##

def connectWeb():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    driver.get(<<<WALLET ADDRESS FROM HIVEOS>>>)
    time.sleep(2)
    refresh = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[1]/div/div/div/div")
    refresh.click()
    return driver

def getUnpaidBalance(driver):

    unpaid = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div/div[1]/div/div[3]/div[1]/div[5]")
    return unpaid.text[:7]

def getExpectedEarnings(driver):

    expected = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div/div[1]/div/div[1]/div[2]")
    return expected.text[:7]

def getTotalPaid(driver):

    paid = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div/div[1]/div/div[4]/div[2]")
    return paid.text[:7]

###### GOOGLE SHEETS API ######

def connectSheet():

    scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name("<<<CREDENTIALS PATH>>>/creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(<<<GOOGLE SHEETS NAME>>>).sheet1

    return sheet

def writeEarnings(sheet,expected,unpaid,total):

    Date = date.today().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M:%S")

    row = [Date, time, expected, unpaid, total]
    sheet.insert_row(row,2)

######## main ###########

DRIVER = connectWeb()
SHEET = connectSheet()

while(1):

    expected = getExpectedEarnings(DRIVER)
    unpaid = getUnpaidBalance(DRIVER)
    total = getTotalPaid(DRIVER)

    writeEarnings(SHEET,expected,unpaid,total)
    time.sleep(43200) #12 horas
