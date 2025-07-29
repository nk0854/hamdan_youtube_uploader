import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

COOKIES_PATH = 'cookies.txt'
COMMUNITY_URL = 'https://www.youtube.com/channel/UC-ocDng1cVqbOUA-BjTE8zw/posts'

def load_cookies(driver, cookies_file):
    print("[INFO] Loading cookies...")
    with open(cookies_file, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) < 7:
                continue
            cookie = {
                'domain': parts[0],
                'name': parts[5],
                'value': parts[6],
                'path': parts[2],
                'secure': parts[3].lower() == 'true',
            }
            if parts[4].isdigit():
                cookie['expiry'] = int(parts[4])
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"[WARNING] Failed to add cookie: {cookie.get('name')} — {e}")

def upload_to_youtube_community(image_path, caption):
    options = Options()
    options.add_argument("--user-agent=Mozilla/5.0")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    try:
        print("[INFO] Opening YouTube...")
        driver.get("https://www.youtube.com")
        time.sleep(5)

        load_cookies(driver, COOKIES_PATH)
        driver.refresh()
        time.sleep(5)

        print("[INFO] Checking login status...")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'avatar-btn')))
        print("[INFO] Login successful.")

        print("[INFO] Navigating to Community tab...")
        driver.get(COMMUNITY_URL)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(5)

        print("[INFO] Clicking image icon...")
        image_post_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(),'Image')]]"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", image_post_button)
        driver.execute_script("arguments[0].click();", image_post_button)
        time.sleep(2)

        print("[INFO] Uploading image...")
        file_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        file_input.send_keys(os.path.abspath(image_path))
        time.sleep(7) 

        print("[INFO] Adding caption...")
        textarea = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true']"))
        )
        driver.execute_script("arguments[0].click();", textarea)
        textarea.send_keys(caption)
        time.sleep(2)

        print("[INFO] Simulating 7x TAB + ENTER to trigger Post...")
        body = driver.find_element(By.TAG_NAME, "body")
        for i in range(7):
            body.send_keys(Keys.TAB)
            time.sleep(1.5)

        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER).perform()

        print("[INFO] Post button clicked. Waiting 60 seconds for processing...")
        time.sleep(60)

        print(f"[SUCCESS] Community post uploaded with image: {image_path}")

    except Exception as e:
        print(f"[ERROR] Failed to post: {str(e)}")
    finally:
        driver.quit()
