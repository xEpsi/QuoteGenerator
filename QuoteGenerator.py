from time import sleep
from base64 import b64decode as api_decode
try:
    import pyautogui
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from colorama import Style, Fore
    pyautogui.move(1,1)
except:#Installs required modules if the they're not already installed
    import os
    print("Whoops, looks like you don't have the required Python modules. Let's fix that.")
    sleep(1)
    os.system('cmd /c "pip install pyautogui"')
    os.system('cmd /c "pip install selenium"')
    os.system('cmd /c "pip install colorama"')
    print("\nPython modules installed!\n")
    import pyautogui
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from colorama import Style, Fore
    print("Successfully imported the required modules. Now starting the program.")
    sleep(1)

amount = int(input(f"{Fore.CYAN}How many quotes do you want to generate? (Please enter a number): "))
print(Style.RESET_ALL)
print("Please do not touch your mouse or keyboard while the program is running.")
loadingtime = 3 #seconds (you're free to change it depending on your PC's speed)

driver = webdriver.Chrome()
driver.get("https://inspirobot.me/")
sleep(loadingtime)
pyautogui.press("f11")
sleep(0.4)

for i in range(amount):
    driver.find_element(By.CLASS_NAME, "btn-text").click()
    sleep(3)
    with open(f'Quote {i+1}.png', 'wb+') as f:
        f.truncate(0)
        f.write(driver.find_element(By.CLASS_NAME, 'generated-image').screenshot_as_png)
    sleep(0.5)

driver.close()

print(f"\n{Fore.LIGHTGREEN_EX}Done!{Style.RESET_ALL}\n")
