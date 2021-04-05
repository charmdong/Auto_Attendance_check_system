from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time

week = input('WEEK : ')
userId = input('input user ID: ');
userPw = input('input user PW: ');

driver = webdriver.Chrome('C:\\Users\\Chung Eastand\\Desktop\\chromedriver')
driver.get("https://blackboard.sejong.ac.kr/webapps/login/")

driver.find_element_by_name('user_id').send_keys(userId)
driver.find_element_by_name('password').send_keys(userPw)

driver.find_element_by_xpath('//*[@id="entry-login"]').click()

driver.get("https://blackboard.sejong.ac.kr/webapps/bbgs-OnlineAttendance-BBLEARN/app/atdView?sortCol=department&numResults=25&course_id=_32462_1&sortDir=DESCENDING")

check = 0
pnp = 0
num = 18012045

print('============== LIST ================')

while num <= 18012054 :
    time.sleep(1)
    if num == 18012045 :
        print(num, 'No Data')
        num += 1
        continue
    try:
        driver.find_element_by_xpath('//*[@id="' + str(num) + '"]').click()
        time.sleep(1)
        data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "listContainer")))
        line = data.text.split("\n")
        for l in line:
            if pnp != 0 :
                if l.find("F") != -1 :
                    print(num, "X")
                    pnp = 0
                    break
                elif l.find("P") != -1 :
                    print(num)
                    pnp = 0
                    break
            if l.find(week+"주차") != -1 :
                pnp += 1
        check = 0
        num += 1
        driver.back()
    except NoSuchElementException:    
        print("No Number")
        check += 1
        num += 1

#driver.find_element_by_xpath('//*[@id="listContainer_nextpage_bot"]').click()
#time.sleep(1)

num = 18012194
check = 0
pnp = 0

while num <= 18012220 :
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="' + str(num) + '"]').click()
        time.sleep(1)
        data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "listContainer")))
        line = data.text.split("\n")
        for l in line:
            if pnp != 0 :
                if l.find("F") != -1 :
                    print(num, "X")
                    pnp = 0
                    break
                elif l.find("P") != -1 :
                    print(num)
                    pnp = 0
                    break
            if l.find(week+"주차") != -1 :
                pnp += 1
        check = 0
        num += 1
        driver.back()
    except NoSuchElementException:    
        #print("No Number")
        #check += 1
        #num += 1
        driver.find_element_by_xpath('//*[@id="listContainer_nextpage_bot"]').click()
        time.sleep(1)
        try :
            driver.find_element_by_xpath('//*[@id="' + str(num) + '"]').click()
            time.sleep(1)
            data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "listContainer")))
            line = data.text.split("\n")
            for l in line:
                if pnp != 0 :
                    if l.find("F") != -1 :
                        print(num, "X")
                        pnp = 0
                        break
                    elif l.find("P") != -1 :
                        print(num)
                        pnp = 0
                        break
                if l.find(week+"주차") != - 1 :
                    pnp+=1
            num += 1
            driver.back()
            driver.find_element_by_xpath('//*[@id="listContainer_prevpage_bot"]').click()
        except NoSuchElementException :
            print("No Number")
            num += 1
            driver.find_element_by_xpath('//*[@id="listContainer_prevpage_bot"]').click()


print('============== DONE ================')
driver.quit()
