# This program will delete all quotes inside the Quotes 
# folder so you don't have to do it manually.

deleteFolder = False

import os
if deleteFolder == True:
    os.rmdir("Quotes")
    print("Deleted folder!")
elif deleteFolder == False:
    for file in os.listdir("Quotes"):
        os.remove(os.path.join("Quotes", file))
    print("Deleted all quotes!")