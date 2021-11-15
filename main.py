import pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray


def hit(key):
    if key == "down":
        pyautogui.keyDown(key)
        time.sleep(0.2)
    pyautogui.press(key)

# def draw():


def isCollide(data):
    for i in range(210, 320):
        for j in range(540, 560):
            if data[i, j] == 172:
                return "down"
    for i in range(240, 360):
        for j in range(620, 650):
            if data[i, j] == 172:
                return "up"
    return False


if __name__ == '__main__':
    print("Games starts in 3 sec")
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            # print(isCollide(data))
            hit(isCollide(data))
        # print(asarray(image))
        # for i in range(240,320):
        #     for j in range(600,650):
        #         data[i,j] = 0
        # image.show()
