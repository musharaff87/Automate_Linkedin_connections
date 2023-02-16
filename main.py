from selenium import webdriver
#import pyautogui
#import requests,webbrowser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from csv import DictWriter
#from bs4 import BeautifulSoup


print("###########################################################################")
print("--------LINKEDIN AUTOMATION TOOL--------")
print("Enter Your Linkedin Mail or Phone Number : ",end=" ")
User_name = input()
print("Enter the password : ",end=" ")
password = input()
print("Now Enter the Keywords for Boolean Search................")
print("Enter The Country or City (eg: canada,texas,sydney,australia ) :",end=" ")
city = input()
print("which field you want to search (eg: it,agriculture,robotics) :",end=" ")
field = input()
print("Enter the role you want to search (eg: manager,owner,developer) :",end=" ")
role = input()
print("Enter the specific content you want to search (eg: business,developer,sydney etc) :",end=" ")
anything = input()
print("Enter the add note you want to send through connection request :",end=" ")
addnote = input()
print("Enter the chrome page you want to search (eg: 0,1,2,3,4,5,6) (note: please enter 0 if its first time search other wise you can change the page you want) : ",end=" " )
page_no = int(input())
print("press close window button if want to stop the program. check the excel sheet after the automation tool is stopped running")
print("Please wait Automation tool is running..............................................................................................")



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
user_but.send_keys(User_name)  # user id
#time.sleep(2)

pass_but = driver.find_element("xpath", '//*[@id="password"]')
pass_but.click()
pass_but.send_keys(password)    # password
pass_but.send_keys(Keys.RETURN)
time.sleep(20) #time gap in seconds


# opening new tab
#pyautogui.hotkey('ctrl', 't')

#nextpage click
#driver.find_element("xpath","//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()


#search starts


search_string = f"site:linkedin.com/in/ + \"{field}\" + \"{role}\" + \"{anything}\" + \"{city}\""

for i in range(7):
    if(i==0):
        matched_elements = driver.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
        time.sleep(50)


        a < 0
        page = page_no
        while a == page:
            driver.find_element("xpath", "//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()
            a = a + 1
            time.sleep(5)

    page_links = driver.find_elements("xpath", "//div[contains(@class, 'yuRUbf')][count(.//a)=1]//a")
    for page in page_links:
        #if(page==page_links[0]):
        #    continue
        print(page.get_attribute("href"))
        cur_page = page.get_attribute("href")
        page.click()
        time.sleep(8)
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
            note.send_keys(f'{addnote}')
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
            note.send_keys(f'{addnote}')
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











