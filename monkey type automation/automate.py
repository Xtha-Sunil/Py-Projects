from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui
import time

class MonkeyTypeAutomation:
    def __init__(self, profile_path, executable_path):
        self.profile_path = profile_path
        self.executable_path = executable_path
        self.driver = self._create_driver()
    
    def _create_driver(self):
        options = Options()
        options.add_argument(f"--user-data-dir={self.profile_path}")
        return webdriver.Chrome(service=Service(executable_path=self.executable_path), options=options)
    
    def automate(self):
        self.driver.get("https://monkeytype.com")
        screen_width, screen_height = pyautogui.size()
        x,y = screen_width/2, screen_height/2+50
        pyautogui.click(x, y)
        not_active = self.driver.find_elements(By.CSS_SELECTOR, ".word:not(.active)")
        not_active_txt = " ".join(elem.text for elem in not_active)
        not_active_txt += " "
        time.sleep(2)
        
        start_time = time.time()
        while time.time() - start_time < 16:
            txt = self.driver.find_element(By.CSS_SELECTOR, ".word.active")
            pyautogui.typewrite(txt.text + " " + not_active_txt)
            not_active_txt = ""


if __name__ == "__main__":
    BASE_PATH = "C:/Users/User/AppData/Local/Google/Chrome/User Data/"
    EXECUTABLE_PATH = "../chromedriver.exe"
    profile = "mainProfile"
    automation = MonkeyTypeAutomation(BASE_PATH+profile, EXECUTABLE_PATH)

    automation.automate()

    input("Enter to finish")
