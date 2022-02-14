# Note: This program will overwrite the existing quotes so make sure to save them in another folder if you want to keep them.

from time import sleep
try:
    import pyautogui
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from colorama import Style, Fore
    from win32com.client import Dispatch
    import os
    import requests
    import zipfile
except:
    print("Error: Run setup.py first.")
    print("Closing in 5 seconds.")
    sleep(5)
    quit()

os.system("cls || clear")
print(Style.RESET_ALL)
dir_name = os.path.dirname(__file__)


#---------- Getting Chrome Version ----------#

def getChromeVersion(filename):
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)
    except Exception:
        return None
    return version

paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
             r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
version = list(filter(None, [getChromeVersion(p) for p in paths]))[0]


#---------- Downloading Chrome Driver ----------#

print(f"{Fore.YELLOW}Testing for Chrome Driver...{Style.RESET_ALL}")
sleep(1)
try:
    if os.path.exists(f"{dir_name}/chromedriver.exe"):
        pass
    else:
        1/0
except:
    try:
        latest_release = str(requests.get(f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{version[:2]}", allow_redirects=True).content)[2:-1]
        latest_url = "https://chromedriver.storage.googleapis.com/{0}/chromedriver_win32.zip".format(latest_release)
        print(f"{Fore.YELLOW}Downloading and extracting the Chrome Driver...\n{Style.RESET_ALL}")
        open('chromedriver_win32.zip', 'wb').write(requests.get(latest_url, allow_redirects=True).content)
        zipfile.ZipFile('chromedriver_win32.zip').extractall()
        os.remove("chromedriver_win32.zip")
        print(f"{Fore.GREEN}Driver successfully downloaded!\n\n{Style.RESET_ALL}")
    except:
        delay=20
        print(f"{Fore.RED}Fatal Error: Failed to download the chrome driver. Please download it at https://chromedriver.chromium.org/downloads according to your chrome version and extract it inside this folder.")
        sleep(3)
        print(f"Closing in {delay} seconds...{Style.RESET_ALL}")
        sleep(delay)
        raise SystemExit


#---------- Getting Quotes ----------#

amount = int(input(f"{Fore.CYAN}How many quotes do you want to generate? (Please enter a number under 50): "))

if amount>=50:
    amount=49

print(f"{Fore.YELLOW}Please do not touch your mouse or keyboard while the program is running.{Style.RESET_ALL}")
loadingtime = 3 #(feel free to change it depending on your PC's loading speed)

driver = webdriver.Chrome()

driver.get("https://inspirobot.me/")
sleep(loadingtime)
pyautogui.press("f11")
sleep(0.4)

for i in range(amount):
    
    driver.find_element(By.CLASS_NAME, "btn-text").click()
    sleep(3)
    if os.path.exists(f"{dir_name}\Quotes"):
        pass
    else:
        os.mkdir(f"{dir_name}\\Quotes")
    quotename = f'{dir_name}\\Quotes\\Quote {i+1}.png'
    with open(quotename, 'wb+') as f:
        f.truncate(0)
        f.write(driver.find_element(By.CLASS_NAME, 'generated-image').screenshot_as_png)
    sleep(0.5)

driver.close()

os.system("cls || clear")
for i in range(5, -1, -1):
    print(f"\n{Fore.LIGHTGREEN_EX}Done! Check the quotes folder.{Style.RESET_ALL}\nClosing in {i}")
    sleep(1)
    os.system("cls || clear")

quit()
