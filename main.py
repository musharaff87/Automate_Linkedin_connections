from selenium import webdriver
import pyautogui
#import requests,webbrowser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from csv import DictWriter
#from bs4 import BeautifulSoup

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

#linkedin sign in

driver.get('https://www.linkedin.com/login')
driver.maximize_window()
time.sleep(2)

user_but = driver.find_element("xpath", '//*[@id="username"]')
user_but.click()
user_but.send_keys('****@gmail.com')  # user id
#time.sleep(2)

pass_but = driver.find_element("xpath", '//*[@id="password"]')
pass_but.click()
pass_but.send_keys('*****')    # password
pass_but.send_keys(Keys.RETURN)
time.sleep(20) #time gap in seconds


# opening new tab
#pyautogui.hotkey('ctrl', 't')

#nextpage click
#driver.find_element("xpath","//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()


#search starts


search_string = "site:linkedin.com/in/ + \"it\" + \"manager\" + \"business\" + \"singapore\""

for i in range(7):
    if(i==0):
        matched_elements = driver.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
        time.sleep(80)


        #a = 0
        #page = 17
        #while a <= page:
        #    driver.find_element("xpath", "//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()
        #    a = a + 1
        #    time.sleep(8)

    page_links = driver.find_elements("xpath", "//div[contains(@class, 'yuRUbf')][count(.//a)=1]//a")
    for page in page_links:
        #if(page==page_links[0]):
        #    continue
        print(page.get_attribute("href"))
        cur_page = page.get_attribute("href")
        page.click()
        time.sleep(10)
        temp = driver.find_elements("xpath", "//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
        l = len(temp)
        print(l)
        linkedin_name = ""
        if(l>9):
            connect = temp[1]
            connect.click()
            time.sleep(2)
            driver.find_element("xpath","//button[contains(@aria-label,'Add a note')]").click()
            time.sleep(2)
            note = driver.find_element("xpath","//textarea[contains(@id,'custom-message')]")
            note.send_keys('Your profile piqued our interest. We "Infogenx Pvt Ltd" is one of the fast growing software development company based in India. Please contact me on Linkedin to discuss about a Business Partnership on profit sharing model for mutual benefit. ')
            time.sleep(2)
            driver.find_element("xpath","//button[contains(@aria-label,'Send now')]").click()
            linkedin_name = ""
            for x in range(len(cur_page)-1,-1,-1):
                if(cur_page[x]=='/'):
                    linkedin_name = cur_page[x+1:len(cur_page)]
                    break
            print(linkedin_name)
        elif(l<=9):
            more = driver.find_elements("xpath","//button[contains(@aria-label,'More actions')]")
            more[1].click()
            time.sleep(2)
            more_con = driver.find_elements("xpath", "//li-icon[contains(@type,'connect')]")
            more_con[1].click()
            time.sleep(2)
            driver.find_element("xpath", "//button[contains(@aria-label,'Add a note')]").click()
            time.sleep(2)
            note = driver.find_element("xpath", "//textarea[contains(@id,'custom-message')]")
            note.send_keys('Your profile piqued our interest. We "Infogenx Pvt Ltd" is one of the fast growing software development company based in India. Please contact me on Linkedin or else tell your best time to discuss about a Business Partnership on profit sharing model for mutual benefit. ')
            time.sleep(2)
            driver.find_element("xpath", "//button[contains(@aria-label,'Send now')]").click()

            for x in range(len(cur_page) - 1, -1, -1):
                if (cur_page[x] == '/'):
                    linkedin_name = cur_page[x + 1:len(cur_page)]
                    break
            print(linkedin_name)
        ###

        field_names = ['NAME', 'CONTACT']

        dict = {'NAME': linkedin_name, 'CONTACT': cur_page}

        with open('Test.csv', 'a') as f_object:

            dictwriter_object = DictWriter(f_object, fieldnames=field_names)

            dictwriter_object.writerow(dict)

            f_object.close()
        ###
        driver.execute_script("window.history.go(-1)")

    driver.find_element("xpath", "//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()











