from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os
import argparse
import schedule
import time
import urllib.request
import zipfile
import platform

webpage = "https://students.genesisedu.com/bernardsboe/sis/view?gohome=true"
cd   = os.getcwd()
name_executable = ""

if platform.system() == "Windows":
    if not os.path.isfile("chromedriver.exe"):
        urllib.request.urlretrieve("https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip", "chromedriver.zip")

        with zipfile.ZipFile("chromedriver.zip", 'r') as zip_ref:
            zip_ref.extractall(cd)
        
        name_executable = "chromedriver.exe"

elif platform.system() == "Linux":
    if not os.path.isfile("chromedriver"):
        urllib.request.urlretrieve("https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip", "chromedriver.zip")

        with zipfile.ZipFile("chromedriver.zip", 'r') as zip_ref:
            zip_ref.extractall(cd)
        
        name_executable = "chromedriver"

else:
    if not os.path.isfile("chromedriver"):
        urllib.request.urlretrieve("https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_mac64.zip", "chromedriver.zip")

        with zipfile.ZipFile("chromedriver.zip", 'r') as zip_ref:
            zip_ref.extractall(cd)
        
        name_executable = "chromedriver"

executable_path = os.path.join(os.getcwd() , name_executable)


def get_arguments():
		parser = argparse.ArgumentParser(description='Genesis Automator')
		parser.add_argument("-e", "--email", dest="email_boe",help="Email of account", required=True)
		parser.add_argument("-p", "--password", dest="password_boe",help="Password of Account", required=True)
		return parser.parse_args()

arguments = get_arguments()

def cmd():
    driver = webdriver.Chrome(executable_path)
    driver.get(webpage)

    s = driver.find_element_by_name("j_username")
    s.send_keys(arguments.email_boe) # email

    s2 = driver.find_element_by_name("j_password")
    s2.send_keys(int(arguments.password_boe)) # student_id

    s3 = driver.find_element_by_class_name("saveButton")
    s3.click()

    s4 = driver.find_element_by_class_name("formButtonIcon")
    s4.click()

    s5 = Select(driver.find_element_by_id('attendanceType'))
    s5.select_by_visible_text('Present')

    s6 = driver.find_element_by_class_name("saveButton")
    s6.click()

schedule.every().day.at("08:00").do(cmd,'It is 08:00. Form filled Successfully')

while True:
    schedule.run_pending()
    time.sleep(30) 