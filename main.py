# If you want to save any quotes, move them into another folder before generating new ones

import requests
from os import path, mkdir
from time import sleep

if not path.isdir("Quotes"):
    mkdir("Quotes")

amount = int(input("Enter the amount of quotes you want to download: "))

for i in range(1, amount+1):
    
    print(f"Downloading quote #{i}...")

    imglink = requests.get("https://inspirobot.me/api?generate=true").text
    img = requests.get(imglink).content

    with open(f"Quotes/Quote {i}.jpg", "wb") as f:
        f.write(img)

print("Download complete!")
print("Closing in 5 seconds...")
sleep(5)
exit()
