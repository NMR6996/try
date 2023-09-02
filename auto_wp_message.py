import random
import time
import pyautogui as pg

animal = ('monkey', 'donkey', 'pig') # I'm just kidding ))

time.sleep(5)
for i in range(50):
    a = random.choice(animal)
    pg.write("you are a " + a)
    pg.press('enter')