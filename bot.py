# ===============[ IMPORTS ]===============
import time
import numpy as np
import pyautogui as ui
from PIL import ImageGrab, ImageOps

# ===============[ MAKING THE DINOSAUR JUMP ]===============
def jump():
    ui.keyDown('space')
    time.sleep(0.05)
    ui.keyUp('space')


# ===============[ DETECTING OBSTACLES AHEAD ]===============
def obstacle_ahead():
    x, y = (300, 400)
    obstacle_box = (x, y, x + 60, y + 30)

    image = ImageGrab.grab(obstacle_box)
    image = ImageOps.grayscale(image)
    image = np.array(image.getcolors())

    if np.sum(image) != 2047:
        return True


# ===============[ MAIN LOOP ]===============
while True:
    if obstacle_ahead():
        jump()
