from os import system
print("Starting setup\n")
try:
  system('cmd /c "pip install pyautogui"')
  system('cmd /c "pip install selenium"')
  system('cmd /c "pip install colorama"')
  system('cmd /c "pip install zipfile"')
  system('cmd /c "pip install requests"')
  print("\nSuccessfully imported the required modules. You can now start the program.")
except:
  print("Error: Failed to install the modules. Try installing them by hand.")
print("NOTE: To install the required module PyWin32, you need to launch cmd as administrator otherwise it won't work.")
