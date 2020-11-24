import pyautogui as pag
import time

textFileDirectory = input("Enter The Text File Directory: ")

print("\nNow Place Your Cursor In The Password Entry Box And Watch The Magic Happen!")

input("\nPress Enter To Continue... ")

time.sleep(3)

with open(textFileDirectory, "r") as f:

        lines = list()

        for line in f:

                lines.append(line)

        for x in lines:

                time.sleep(0.25)
        
                pag.write(x)

                pag.press("return")





































