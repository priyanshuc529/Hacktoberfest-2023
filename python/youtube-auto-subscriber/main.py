from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
from tqdm import tqdm
import msvcrt
from multiprocessing import freeze_support

# YouTube Channel ID List
with open('channel_ids.txt', 'r') as file:
    channel_ids = [line.strip() for line in file.readlines()]

# ID, PW for Google(Youtube) login
user_info = {}
with open('user_info.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        key, value = line.strip().split(' = ')
        user_info[key] = value
username = user_info['username']
password = user_info['password']

def init_driver():
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    driver = uc.Chrome(options=options)
    return driver


def youtube_login(driver):
    print("Start Login")
    driver.get('https://accounts.google.com/ServiceLogin')

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'identifierId'))
    )
    email_input.send_keys(username)
    next_button = driver.find_element(By.ID, 'identifierNext')
    next_button.click()
    time.sleep(5)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'Passwd'))
    )
    password_input.send_keys(password)
    login_button = driver.find_element(By.ID, 'passwordNext')
    login_button.click()
    time.sleep(5)
    driver.get('https://myaccount.google.com/personal-info')
    expected_username = username + '@gmail.com'
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/c-wiz/section/div[3]/div/div/div[2]/div/a/div/div[1]/div/div[2]/div/div'))
    )
    if element.text == expected_username:
        print("Login Success")
    else:
        print("Login Failed")

def youtube_subscribe(driver):
    print(f"Start Subscribing")
    cnt = 0
    for channel_id in tqdm(channel_ids):
        channel_url = f'https://www.youtube.com/channel/{channel_id}'

        try:
            driver.get(channel_url)

            subscribed_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="text"]'))
            )
            youtube_name = subscribed_message.text

            subscribe_button = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.ID, 'subscribe-button'))
            )
            subscribe_button.click()
            print(f"Subscribe {youtube_name}")
            cnt += 1
        except:
            print(f"Non-existent channel id: {channel_id}")
            continue
    print(f"Done\nSubscribe {cnt} channel(s)")

def program_exit(driver):
    driver.quit()
    print("Press any key to close...")
    msvcrt.getch()
    exit()

if  __name__  ==  "__main__":
    try:
        freeze_support()
        driver = init_driver()
        youtube_login(driver)
        youtube_subscribe(driver)
    except Exception as e:
        print("An Error Occurred:", e)
    program_exit(driver)