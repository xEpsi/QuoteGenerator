from os import system
print("Starting setup\n")
try:
  system('cmd /c "pip install pyautogui"')
  system('cmd /c "pip install selenium"')
  system('cmd /c "pip install colorama"')
  print("\nSuccessfully imported the required modules. You can now start the program.")
except:
  print("Error: Failed to install the modules. Try installing them by hand.")
