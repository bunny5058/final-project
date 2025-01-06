from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
# import undetected_chromedriver as uc
# from fake_useragent import UserAgent
def main():
        url = "https://www.irctc.co.in/nget/train-search"
        ses=details()
        driver = webdriver.Chrome()
        driver.implicitly_wait(100)
        driver.get(url)
        form_fill(driver,ses,url)
        login(driver,ses)
        train_select(driver)
        pass_details(driver)
        input("Wait")
        #form_fill(driver,ses,url)


def login(driver,ses,):
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[1]/app-header/div[1]/div[2]").click()
        driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='User Name']").send_keys(ses["username"])
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(ses["password"])
        time.sleep(20)
        #input("Wait")
        #form_fill(driver,ses,url)
        # fill capcha manually then click sign 

def get_input(prompt,pattern):
    while True:
        value = input(prompt)
        if re.match(pattern, value):
            return value
        print("Invalid input")
       

def details():
    ses = {
        "username": get_input("Enter username: ",r"^[a-zA-Z0-9_]+$"),
        "password": get_input("Enter password: ",r"^[a-zA-Z0-9_]+$"),
        "from": get_input("Enter departure station code: ",r"^[A-Z]{3,5}$"),
        "to": get_input("Enter destination station code: ",r"^[A-Z]{3,5}$"),
        "jdate": get_input("Enter journey date (DD/MM/YYYY): ",r"^\d{2}/\d{2}/\d{4}$"),
        "class": get_input("Enter class: ",r"^[1-3]A$"),
        "cat": get_input("Enter category: ",r"^[A-Z]+$")
    }
    return ses

def form_fill(driver,ses,url):
            #url = "https://www.irctc.co.in/nget/train-search"

            #ses = {
                #"username": "indierahul",
                #"password": "raRA12345",
                #"from": "NDLS",
                #"to": "BUI",
                #"jdate": "31/12/2024",
                #"class": "2A",
                #"cat": "GENERAL"
                  #}
            #driver = webdriver.Chrome()
            driver.implicitly_wait(100)
            driver.get(url)

            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.ESCAPE)

            frm = driver.switch_to.active_element
            frm.send_keys(ses["from"])
            time.sleep(1)
            frm.send_keys(Keys.ENTER)

            time.sleep(1)

            frm.send_keys(Keys.TAB)
            driver.switch_to.active_element.send_keys(Keys.TAB)


            to_station = driver.switch_to.active_element
            to_station.send_keys(ses["to"])
            time.sleep(1)
            to_station.send_keys(Keys.ENTER)
            to_station.send_keys(Keys.TAB)

            jdate = driver.switch_to.active_element
            jdate.send_keys(ses["jdate"])
            driver.switch_to.active_element.send_keys(Keys.ESCAPE)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
        

            classes = driver.switch_to.active_element
            #driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
            for  i in range(5):
                driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
            classes.send_keys(Keys.TAB)
            time.sleep(1)
            category = driver.switch_to.active_element
            time.sleep(1)
            category.send_keys(ses["cat"])
            cat=driver.switch_to.active_element
            time.sleep(1)
            cat.send_keys(Keys.TAB)
            driver.switch_to.active_element.send_keys(Keys.ENTER)

            #input("Wait")
def train_select(driver):
        refresh=driver.find_element(By.XPATH,"//span[@class='fa fa-repeat']")
        refresh.click()
        select=driver.find_element(By.XPATH,"/html/body/app-root/app-home/div[3]/div/app-train-list/div[4]/div/div[5]/div[3]/div[1]/app-train-avl-enq/div[1]/div[7]/div[1]/div[3]/table/tr/td[2]/div")
        select.click()
        Book=driver.find_element(By.XPATH,"//button[@class='btnDefault train_Search ng-star-inserted']")
        Book.click()
def pass_details(driver):
    wait = WebDriverWait(driver, 10)
    
    #Wait for the first input field to be interactable and fill it
    pass_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Name']")))
    pass_name.send_keys("rahul")
    time.sleep(1)
    pass_Age = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Age']")))
    pass_Age.send_keys("22")
    print("1")
    time.sleep(1)
    pass_gender=wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@formcontrolname='passengerGender']")))
    pass_gender.send_keys(Keys.ARROW_DOWN)
    print("2")
    j=1  
    for i in range(7):
        time.sleep(1)
        if j==4:
            print("4")
            veg=driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
            pass
        else:
            press=driver.switch_to.active_element.send_keys(Keys.TAB)
            j=j+1

        print("3")
    m_no=driver.switch_to.active_element.send_keys("8882049614")
 
    for i in range(7):
        press=driver.switch_to.active_element.send_keys(Keys.TAB)   
    conti=driver.switch_to.active_element
    conti.click()
    input("Wait")
    #Use ActionChains to navigate through the form
    # actions = ActionChains(driver)
    # actions.send_keys(Keys.TAB).perform()
    # actions.send_keys(Keys.TAB).perform()
    # actions.send_keys(Keys.ARROW_DOWN).perform()
    # actions.send_keys(Keys.ENTER).perform()
    
    # for _ in range(7):
    #     actions.send_keys(Keys.TAB).perform()
    
    # # Fill the mobile number
    # M_no = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Mobile Number']")))
    # M_no.send_keys("8882049614")
    
    # for _ in range(7):
    #     actions.send_keys(Keys.TAB).perform()
    
    # actions.send_keys(Keys.ENTER).perform()
    #input("Wait")
# def pass_details(driver):
#         pass_name=driver.switch_to.active_element.send_keys(Keys.TAB)
#         pass_name1=driver.switch_to.active_element.send_keys(Keys.TAB)
#         pass_name2=driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
#         driver.switch_to.active_element.send_keys(Keys.ENTER)
#         for i in range (7):
#             pass_name=driver.switch_to.active_element.send_keys(Keys.TAB)
#         M_no=driver.switch_to.active_element.send_keys("8882049614")
#         for i in range (7):
#             cont=driver.switch_to.active_element.send_keys(Keys.TAB)
#         count=driver.switch_to.active_element.send_keys(Keys.ENTER)
#         input("Wait")   
# driver.find_element(By.XPATH, xpath).click()

#input("Wait")
# driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[1]/app-header/div[1]/div[2]").click()
# driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()
# driver.find_element(By.XPATH, "//input[@placeholder='User Name']").send_keys(ses["username"])
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(ses["password"])
#   time.sleep(20)
# fill capcha manually then click sign in
#try:
    #xpath = "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/input"
    #var=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    
    #var.send_keys("ABX")
    #driver.find_element(By.XPATH, "//input[@aria-controls='pr_id_1_list'").click()
    #from_station = driver.find_element(By.XPATH, "//p[.//label[text()='From']]")
    #from_station.find_element(By.TAG_NAME, "input").send_keys(ses["from"])

    #to_station = driver.find_element(By.XPATH, "//p[.//label[text()='To']]")
    #to_station.find_element(By.TAG_NAME, "input").send_keys(ses["to"])

    #j_date = driver.find_element(By.XPATH, "//p[.//label[contains[text(), 'DD/MM/YYYY']]]")
    #j_date.find_element(By.TAG_NAME, "input").send_keys(ses["jdate"])

    #input("wait")

# except:
#         raise  ElementNotInteractableException("element is not intractable ")


#         logout_span = WebDriverWait(driver, 100).until(
#             EC.text_to_be_present_in_element(
#                 (By.CSS_SELECTOR, "span.list_text > label > b"), "Logout"
#             )
#         )
if __name__ == "__main__":
    main()