import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


def driver_setup():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")
    options.add_argument("--user-data-dir=C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("--profile-directory=Profile 2")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver_menu(driver)


def driver_menu(driver):
    time.sleep(3)
    print("Scraping the web all the time ---" + "\n" + "[1]ChatGPT 3.5" + "\n" + "[2]Google Palm" + "\n" + "[3]Poe Assistant")
    user_choice = input()
    if user_choice == "1":
        access_poe_ChatGPT3_0(driver)
    else:
        print("Invalid Input")
        input()
        driver_menu(driver)

def Chat_keywords(input, driver):
    if input == "/close":
        driver.quit()
        return input
    elif input == "/return":
        driver_menu(driver)
        return input
    elif input == "/clear":
        os.Clear()
    else:
        return input

def access_poe_ChatGPT3_0(driver):
    url = "https://poe.com/ChatGPT"
    driver.get(url)
    try:
        wait_website = WebDriverWait(driver, 10)
        wait_website.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[class*='GrowingTextArea_textArea__eadlu']")))
    except Exception as ex:
        print("Website failed to load after 10 seconds" + "\n" + str(ex))
        input()
        driver_menu(driver)

    while True:
        user_inputMSG = input("Input your Message: ")
        user_inputMSG = Chat_keywords(user_inputMSG, driver)

        chat_box_layer = driver.find_element(By.CSS_SELECTOR, "div[class*='GrowingTextArea_growWrap___1PZM ChatMessageInputContainer_textArea__kxuJi']")
        chat_box_inpout = driver.find_element(By.CSS_SELECTOR, "textarea[class*='GrowingTextArea_textArea__eadlu']")
        chat_box_inpout.send_keys(user_inputMSG)

        try:
            wait_button = WebDriverWait(driver, 10)
            submit_button = wait_button.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='Button_buttonBase__0QP_m Button_primary__pIDjn ChatMessageSendButton_sendButton__OMyK1 ChatMessageInputContainer_sendButton__s7XkP']")))
            submit_button.click()
        except Exception as ex:
            print("Button did not become clickable" + str(ex))
            return

        try:
            wait_msgComplete = WebDriverWait(driver, 30)
            wait_msgComplete.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button[class*='Button_buttonBase__0QP_m Button_chatShare__Ehzog']")))
        except Exception as ex:
            print("Message failed to send" + str(ex))
            return

        chatMsgElements = driver.find_elements(By.CSS_SELECTOR,"div[class*='Markdown_markdownContainer__UyYrv']")
        if len(chatMsgElements) > 0:
            latestChatMsgElement = chatMsgElements[-1]
            latestChatMsgText = latestChatMsgElement.text

            print("\n" + "ChatGPT: " + latestChatMsgText + "\n")
        else:
            print("No chat messages found.")

        
driver_setup()